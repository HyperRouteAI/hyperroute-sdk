import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { HyperRoute, ApiError, JobError, ProtocolError, RequestTimeout, CancelledError } from '../dist/index.js';
const fix = JSON.parse(readFileSync(new URL('../../contract/fixtures.json',import.meta.url)));
const api = JSON.parse(readFileSync(new URL('../../contract/openapi.json',import.meta.url)));
const json = (data,status=200,headers={}) => new Response(JSON.stringify(data),{status,headers:{'content-type':'application/json',...headers}});

test('authentication, request, metadata and unknown fields',async()=>{
  const client=new HyperRoute({apiKey:'test-token',fetch:async(url,init)=>{
    assert.equal(init.headers.get('authorization'),'Bearer test-token');
    assert.deepEqual(JSON.parse(init.body),{query:'hello'});
    assert.equal(init.redirect,'manual');
    return json(fix.recommendation,200,{'x-caller-ref':'ref-1'});
  }});
  const result=await client.recommend({query:'hello'});
  assert.deepEqual(result.data,fix.recommendation);
  assert.equal(result.headers.get('x-caller-ref'),'ref-1');
});

test('errors preserve bodies, mutations are not retried, business errors are data',async()=>{
  let calls=0;
  const client=new HyperRoute({maxRetries:3,fetch:async()=>{calls++;return json(fix.error,503);}});
  await assert.rejects(client.execute({tool_id:'t',query:'q'}),e=>e instanceof ApiError && e.statusCode===503 && e.body.detail.error==='unauthorized');
  assert.equal(calls,1);
  const response=await new HyperRoute({fetch:async()=>json(fix.execution)}).execute({tool_id:'t',query:'q'});
  assert.equal(response.data.ok,false);
});

test('GET retry and Retry-After budget',async()=>{
  let calls=0;
  const client=new HyperRoute({maxRetries:1,fetch:async()=>++calls===1?json({},503,{'retry-after':'0'}):json(fix.health)});
  assert.equal((await client.health()).data.ready,true);
  assert.equal(calls,2);
  calls=0;
  await assert.rejects(new HyperRoute({maxRetries:2,timeoutMs:10,fetch:async()=>{calls++;return json({},429,{'retry-after':'1000'});}}).health(),ApiError);
  assert.equal(calls,1);
});

test('timeouts and cancellation',async()=>{
  const fetch=async(url,init)=>new Promise((resolve,reject)=>{
    init.signal.addEventListener('abort',()=>reject(init.signal.reason),{once:true});
    const timer=setTimeout(()=>resolve(json({})),100);
    init.signal.addEventListener('abort',()=>clearTimeout(timer),{once:true});
  });
  await assert.rejects(new HyperRoute({fetch,timeoutMs:5}).health(),RequestTimeout);
  const controller=new AbortController();controller.abort();
  await assert.rejects(new HyperRoute({fetch}).health({signal:controller.signal}),CancelledError);
});

test('polling uses existing job and handles failure',async()=>{
  let calls=0;
  const client=new HyperRoute({fetch:async(url,init)=>{
    assert.equal(init.method,'GET');
    return json(++calls===1?fix.queued:{state:'done',result:fix.recommendation});
  }});
  assert.deepEqual((await client.waitForRecommendation('job-1',{pollIntervalMs:1})).data,fix.recommendation);
  await assert.rejects(new HyperRoute({fetch:async()=>json({state:'error',error:'failed'})}).waitForRecommendation('j'),JobError);
  await assert.rejects(new HyperRoute({fetch:async()=>json({state:'unknown'})}).waitForRecommendation('j'),ProtocolError);
});

function stream(text) {
  const bytes=new TextEncoder().encode(text);
  return new Response(new ReadableStream({start(controller){for(let i=0;i<bytes.length;i+=3)controller.enqueue(bytes.slice(i,i+3));controller.close();}}),{headers:{'content-type':'text/event-stream'}});
}
test('fragmented UTF-8, CRLF, multiline data and completion',async()=>{
  const payload={...fix.recommendation,note:'café'};
  const text=': heartbeat\r\nevent: queued\r\ndata: {"state":\r\ndata: "queued"}\r\n\r\nevent: result\r\ndata: '+JSON.stringify(payload)+'\r\n\r\n';
  const events=[];
  for await(const e of new HyperRoute({fetch:async()=>stream(text)}).streamRecommendation({query:'q'}))events.push(e);
  assert.deepEqual(events.map(e=>e.event),['queued','result']);
  assert.deepEqual(events[1].data,payload);
});

test('stream failures, premature EOF and malformed JSON',async()=>{
  for(const [text,ErrorType] of [['',ProtocolError],['event: error\ndata: {"error":"failed"}\n\n',JobError],['event: result\ndata: bad\n\n',ProtocolError]]){
    await assert.rejects(async()=>{for await(const e of new HyperRoute({fetch:async()=>stream(text)}).streamRecommendation({query:'q'})){}},ErrorType);
  }
});

test('text, bytes and escaped path',async()=>{
  const seen=[];
  const client=new HyperRoute({fetch:async(url)=>{seen.push(String(url));return new Response('hello',{headers:{'content-type':'text/plain'}});}});
  assert.equal((await client.console()).data,'hello');
  assert.deepEqual((await client.downloadResult('a/b ?')).data,new TextEncoder().encode('hello'));
  assert.ok(seen[1].endsWith('/result/a%2Fb%20%3F'));
});

test('all operation methods match the shared contract',async()=>{
  const seen=[];
  const client=new HyperRoute({fetch:async(url,init)=>{seen.push({url:new URL(url),init});return json({});}});
  for(const [path,methods] of Object.entries(api.paths))for(const [method,op] of Object.entries(methods)){
    const args=op.parameters.filter(p=>p.in==='path').map(()=>'identifier');
    if(op.requestBody)args.push({query:'fixture'});
    const query=Object.fromEntries(op.parameters.filter(p=>p.in==='query').map(p=>[p.name,'value']));
    if(Object.keys(query).length)args.push(query);
    const name=op.operationId.replace(/_([a-z])/g,(_,c)=>c.toUpperCase());
    await client[name](...args);
    const {url,init}=seen.at(-1);
    assert.equal(init.method,method.toUpperCase());
    assert.equal(url.pathname,path.replace(/\{[^}]+\}/g,'identifier'));
    assert.deepEqual(Object.fromEntries(url.searchParams),query);
    if(op.requestBody)assert.deepEqual(JSON.parse(init.body),{query:'fixture'});
  }
});
