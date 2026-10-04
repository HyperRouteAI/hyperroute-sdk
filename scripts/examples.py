import json
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
fixtures=json.loads((ROOT/'contract/fixtures.json').read_text())
seen=[]


class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args):
        pass

    def respond(self,body,code=200,content_type='application/json'):
        data=body.encode() if isinstance(body,str) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header('content-type',content_type)
        self.send_header('content-length',str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        seen.append(('GET',self.path))
        if self.path.startswith('/recommend/status/'):
            self.respond({'job':'job-1','state':'done','lane':'recommend','position':None,'lane_position':None,'eta_ms':0,'result':fixtures['recommendation']})
        else:
            self.respond(fixtures['health'])

    def do_POST(self):
        body=json.loads(self.rfile.read(int(self.headers.get('content-length',0))) or b'{}')
        seen.append(('POST',self.path))
        if self.path=='/recommend/submit':
            self.respond(fixtures['queued'],202)
        elif self.path=='/recommend':
            rec=fixtures[{'full':'full_recommendation','min':'min_recommendation'}.get(body.get('detail'),'recommendation')]
            if self.headers.get('accept')=='text/event-stream':
                self.respond('event: result\ndata: '+json.dumps(rec)+'\n\n',content_type='text/event-stream')
            elif body.get('format')=='text':
                self.respond('Example Search: Search research',content_type='text/plain')
            else:
                self.respond(rec)
        elif self.path=='/execute':
            assert body['tool_id']=='example_search'
            self.respond(fixtures['execution'])
        elif self.path=='/report_outcome':
            assert body['session_id']=='session-1'
            self.respond({'ok':True,'session_id':'session-1','tool_id':'example_search','accepted':{'score':body['score'],'reason':None,'counts_as_quality':True,'quality':1.0,'comment':False,'human_survey':False},'field_probe':None,'triggers_raised':[],'score_moved':False})
        else:
            self.respond({'error':'unexpected_path'},404)


def main():
    server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
    thread=threading.Thread(target=server.serve_forever,daemon=True)
    thread.start()
    env={**os.environ,'HYPERROUTE_BASE_URL':f'http://127.0.0.1:{server.server_port}','HYPERROUTE_API_KEY':'fixture-token'}
    try:
        for language in sys.argv[1:] or ['python','typescript']:
            folder=ROOT/'examples'/language
            for path in sorted(folder.glob('*.py' if language=='python' else '*.mjs')):
                args=[sys.executable if language=='python' else 'node',str(path)]
                if path.stem=='execute':args+=['--execute','--tool-id','example_search','--session-id','session-1','--query','fixture']
                if path.stem=='feedback':args+=['--session-id','session-1','--tool-id','example_search','--score','full']
                subprocess.run(args,env=env,check=True,stdout=subprocess.DEVNULL,timeout=20)
                print(f'Passed {language}/{path.name}')
    finally:
        server.shutdown()
        server.server_close()
    assert seen


if __name__ == "__main__":
    main()
