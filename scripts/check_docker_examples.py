import argparse
import json
import os
import shlex
import subprocess
import threading
import uuid
from http.server import ThreadingHTTPServer
from pathlib import Path

from examples import Handler, fixtures

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--live',action='store_true')
parser.add_argument('--language',choices=['python','typescript'])
args=parser.parse_args()
result_dir=ROOT/'test-results'/'docker'
result_dir.mkdir(parents=True,exist_ok=True)
server=None
if args.live:
    endpoint='https://hyperroute.io'
else:
    server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
    threading.Thread(target=server.serve_forever,daemon=True).start()
    endpoint=f'http://127.0.0.1:{server.server_port}'
mode='live' if args.live else 'fixture'
failures=[]
try:
    for language in [args.language] if args.language else ['python','typescript']:
        folder=ROOT/'examples'/language
        extension='.py' if language=='python' else '.mjs'
        files=[p for p in sorted(folder.glob('*'+extension)) if not args.live or p.stem not in {'execute','feedback'}]
        image='python:3.12-slim' if language=='python' else 'node:22-slim'
        package_dir=ROOT/'python/dist' if language=='python' else ROOT/'typescript'
        packages=list(package_dir.glob('*.whl' if language=='python' else '*.tgz'))
        assert len(packages)==1,f'Build exactly one {language} distribution first'
        package=packages[0]
        setup=(f'python -m pip install --no-cache-dir --disable-pip-version-check --target /tmp/installed /package/{shlex.quote(package.name)} >&2' if language=='python' else f'npm install --prefix /tmp/app --ignore-scripts --no-audit --no-fund /package/{shlex.quote(package.name)} >&2\nmkdir -p /tmp/app/examples\ncp /examples/*.mjs /tmp/app/examples/')
        commands=['set -eu',setup]
        for path in files:
            executable='python' if language=='python' else 'node'
            location='/examples/' if language=='python' else '/tmp/app/examples/'
            argv=[executable,location+path.name]
            if path.stem=='execute':argv+=['--execute','--tool-id','example_search','--session-id','session-1','--query','fixture']
            if path.stem=='feedback':argv+=['--session-id','session-1','--tool-id','example_search','--score','full']
            commands.append('printf "%s\\n" '+shlex.quote('SDK_EXAMPLE_START '+path.name))
            commands.append('if '+shlex.join(argv)+'; then printf "%s\\n" "SDK_EXAMPLE_EXIT 0"; else printf "%s\\n" "SDK_EXAMPLE_EXIT 1"; fi')
        container_name='hyperroute-sdk-test-'+uuid.uuid4().hex[:12]
        docker=['docker','run','--rm','--name',container_name,'--network','host','--read-only','--cap-drop','ALL','--security-opt','no-new-privileges','--tmpfs','/tmp:rw,exec,size=268435456','--env','HYPERROUTE_BASE_URL='+endpoint,'--env','PYTHONDONTWRITEBYTECODE=1','--env','PYTHONPATH=/tmp/installed','--env','npm_config_cache=/tmp/npm-cache','--mount',f'type=bind,src={package},dst=/package/{package.name},readonly','--mount',f'type=bind,src={folder},dst=/examples,readonly',image,'sh','-c','\n'.join(commands)]
        try:
            result=subprocess.run(docker,capture_output=True,text=True,timeout=900)
        finally:
            subprocess.run(['docker','rm','-f',container_name],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        (result_dir/f'{language}-{mode}.stdout.txt').write_text(result.stdout)
        (result_dir/f'{language}-{mode}.stderr.txt').write_text(result.stderr)
        current=None
        outputs={}
        for line in result.stdout.splitlines():
            if line.startswith('SDK_EXAMPLE_START '):
                current=line.split(' ',1)[1];outputs[current]={'stdout':[]}
            elif line.startswith('SDK_EXAMPLE_EXIT ') and current:
                code=int(line.split(' ',1)[1]);outputs[current]['exit_code']=code
                if code:failures.append(language+'/'+current)
                print(f'{language}/{current}: '+('passed' if code==0 else 'failed'),flush=True)
                current=None
            elif current:outputs[current]['stdout'].append(line)
        if result.returncode or len(outputs)!=len(files) or any('exit_code' not in item for item in outputs.values()):
            failures.append(language+' container')
            print(result.stderr[-4000:],flush=True)
        (result_dir/f'{language}-{mode}.json').write_text(json.dumps(outputs,indent=2)+'\n')
        if not args.live:
            expected={'recommend':'recommendation','async_recommend':'recommendation','poll':'recommendation','evidence':'full_recommendation','minimal':'min_recommendation','execute':'execution'}
            for filename,item in outputs.items():
                stem=Path(filename).stem
                output='\n'.join(item['stdout'])
                if stem in expected:
                    assert json.loads(output)==fixtures[expected[stem]],f'{language}/{filename} omitted response fields'
                elif stem=='stream':
                    assert json.loads(output)=={'event':'result','data':fixtures['recommendation']},f'{language}/{filename} omitted event fields'
                elif stem=='text':
                    assert output=='Example Search: Search research'

finally:
    if server:
        server.shutdown();server.server_close()
if failures:raise SystemExit('Failed: '+', '.join(failures))
