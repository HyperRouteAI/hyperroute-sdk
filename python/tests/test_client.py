import asyncio
import json
import threading
from pathlib import Path

import httpx
import pytest
from hyperroute import HyperRoute, AsyncHyperRoute, ApiError, RequestOptions, RequestTimeout, CancelledError, ProtocolError, JobError

ROOT = Path(__file__).resolve().parents[2]
FIX = json.loads((ROOT/'contract/fixtures.json').read_text())
API = json.loads((ROOT/'contract/openapi.json').read_text())


def client(handler, **kwargs):
    return HyperRoute(api_key='test-token', http_client=httpx.Client(transport=httpx.MockTransport(handler)), **kwargs)


def test_auth_body_headers_and_forward_fields():
    def handle(req):
        assert req.headers['authorization'] == 'Bearer test-token'
        assert req.headers['x-hyperroute-surface'] == 'sdk-python'
        assert json.loads(req.content) == {'query':'hello'}
        return httpx.Response(200,json=FIX['recommendation'],headers={'x-caller-ref':'ref-1'})
    result = client(handle).recommend({'query':'hello'})
    assert result.data['extra_field']['preserved']
    assert result.headers['x-caller-ref'] == 'ref-1'


@pytest.mark.parametrize('status',[401,422,429,500])
def test_errors_preserve_body_without_exposing_it_in_message(status):
    with pytest.raises(ApiError) as caught:
        client(lambda r:httpx.Response(status,json=FIX['error'])).execute({'tool_id':'t','query':'q'})
    assert caught.value.body == FIX['error']
    assert caught.value.status_code == status
    assert 'Authentication required' not in str(caught.value)


def test_business_error_is_data_and_mutations_never_retry():
    calls=[]
    def handler(req):
        calls.append(req)
        return httpx.Response(503,json=FIX['error'])
    with pytest.raises(ApiError):
        client(handler,max_retries=3).execute({'tool_id':'t','query':'q'})
    assert len(calls)==1
    result=client(lambda r:httpx.Response(200,json=FIX['execution'])).execute({'tool_id':'t','query':'q'})
    assert result.data['ok'] is False


def test_get_retries_and_retry_after_budget():
    calls=[]
    def handler(req):
        calls.append(req)
        return httpx.Response(503,json={},headers={'retry-after':'0'}) if len(calls)==1 else httpx.Response(200,json=FIX['health'])
    assert client(handler,max_retries=1).health().data['ready']
    assert len(calls)==2
    calls.clear()
    with pytest.raises(ApiError):
        client(lambda r:(calls.append(r) or httpx.Response(429,json={},headers={'retry-after':'1000'})),max_retries=3,timeout=1).health()
    assert len(calls)==1


def test_text_bytes_encoding_and_cancellation():
    seen=[]
    c=client(lambda r:(seen.append(r) or httpx.Response(200,content=b'hello',headers={'content-type':'text/plain'})))
    assert c.console().data=='hello'
    assert c.download_result('a/b ?').data==b'hello'
    assert seen[-1].url.raw_path==b'/result/a%2Fb%20%3F'
    stopped=threading.Event(); stopped.set()
    with pytest.raises(CancelledError):
        c.health(options=RequestOptions(cancel=stopped))
    assert len(seen)==2


def test_no_redirects():
    seen=[]
    with pytest.raises(ApiError) as caught:
        client(lambda r:(seen.append(r) or httpx.Response(307,headers={'location':'https://other.invalid'},text='redirect'))).health()
    assert caught.value.status_code==307
    assert len(seen)==1


def test_poll_never_resubmits_and_errors():
    seen=[]
    def handler(r):
        seen.append(r)
        return httpx.Response(200,json=FIX['queued'] if len(seen)==1 else {'job':'job-1','state':'done','result':FIX['recommendation']})
    assert client(handler).wait_for_recommendation('job-1',poll_interval=.001).data==FIX['recommendation']
    assert all(r.method=='GET' for r in seen)
    with pytest.raises(JobError):
        client(lambda r:httpx.Response(200,json={'state':'error','error':'failed'})).wait_for_recommendation('job-1')
    with pytest.raises(ProtocolError):
        client(lambda r:httpx.Response(200,json={'state':'unknown'})).wait_for_recommendation('job-1')


@pytest.mark.parametrize('suffix,error',[('',ProtocolError),('event: error\ndata: {"error":"failed"}\n\n',JobError),('event: result\ndata: invalid\n\n',ProtocolError)])
def test_stream_failures(suffix,error):
    with pytest.raises(error):
        list(client(lambda r:httpx.Response(200,text=': heartbeat\n\n'+suffix,headers={'content-type':'text/event-stream'})).stream_recommendation({'query':'q'}))


def test_stream_multiline_and_terminal_result():
    text=': heartbeat\r\nevent: queued\r\ndata: {"state":\r\ndata: "queued"}\r\n\r\nevent: result\r\ndata: '+json.dumps(FIX['recommendation'])+'\r\n\r\n'
    events=list(client(lambda r:httpx.Response(200,text=text,headers={'content-type':'text/event-stream'})).stream_recommendation({'query':'q'}))
    assert [e.event for e in events]==['queued','result']
    assert events[-1].data==FIX['recommendation']


async def test_async_cancel_timeout_retry_poll_stream():
    seen=[]
    async def slow(r):
        await asyncio.sleep(1)
        return httpx.Response(200,json={})
    c=AsyncHyperRoute(http_client=httpx.AsyncClient(transport=httpx.MockTransport(slow)),timeout=.01)
    with pytest.raises(RequestTimeout):
        await c.health()
    task=asyncio.create_task(c.health())
    await asyncio.sleep(0)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    async def handle(r):
        seen.append(r)
        if r.headers.get('accept')=='text/event-stream':
            return httpx.Response(200,text='event: result\ndata: '+json.dumps(FIX['recommendation'])+'\n\n',headers={'content-type':'text/event-stream'})
        if len(seen)==1:
            return httpx.Response(503,json={},headers={'retry-after':'0'})
        return httpx.Response(200,json={'job':'j','state':'done','result':FIX['recommendation']})
    c=AsyncHyperRoute(http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle)),max_retries=1)
    assert (await c.wait_for_recommendation('j')).data==FIX['recommendation']
    assert [e.data async for e in c.stream_recommendation({'query':'q'})]==[FIX['recommendation']]


@pytest.mark.parametrize('asynchronous',[False,True])
async def test_every_operation_matches_contract(asynchronous):
    seen=[]
    handler=lambda r:(seen.append(r) or httpx.Response(200,json={}))
    c=AsyncHyperRoute(http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler))) if asynchronous else client(handler)
    for path, methods in API['paths'].items():
        for method, op in methods.items():
            args=[]
            for p in op.get('parameters',[]):
                if p['in']=='path':args.append('identifier')
            if 'requestBody' in op:args.append({'query':'fixture'})
            query={p['name']:'value' for p in op.get('parameters',[]) if p['in']=='query'}
            if query:args.append(query)
            out=getattr(c,op['operationId'])(*args)
            if asynchronous:await out
            req=seen[-1]
            assert req.method==method.upper()
            import re
            assert req.url.path==re.sub(r'\{[^}]+\}','identifier',path)
            assert dict(req.url.params)==query
            if 'requestBody' in op:assert json.loads(req.content)=={'query':'fixture'}


def test_bad_configuration_and_invalid_json():
    for kwargs in [{'timeout':0},{'max_retries':-1},{'base_url':'http://remote.invalid'},{'base_url':'https://token@host.invalid'}]:
        with pytest.raises(ValueError):HyperRoute(**kwargs)
    with pytest.raises(ProtocolError):
        client(lambda r:httpx.Response(200,text='not JSON')).health()
