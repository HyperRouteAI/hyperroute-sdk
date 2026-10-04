import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wheels=list((ROOT/'python/dist').glob('*.whl'))
assert len(wheels)==1,'Build exactly one Python wheel first'
with tempfile.TemporaryDirectory() as temp:
    stage=Path(temp)
    target=stage/'python'
    subprocess.run([sys.executable,'-m','pip','install','--no-deps','--target',str(target),str(wheels[0])],check=True,stdout=subprocess.DEVNULL)
    code="from pathlib import Path; import hyperroute; from hyperroute.types import FullRecommendation, ProbeEvidence; assert Path(hyperroute.__file__).is_relative_to(Path(__import__('os').environ['SDK_PACKAGE_TARGET'])); assert (Path(hyperroute.__file__).parent/'py.typed').exists(); print('Python wheel import and typing metadata verified')"
    subprocess.run([sys.executable,'-c',code],cwd=temp,env={**os.environ,'PYTHONPATH':str(target),'SDK_PACKAGE_TARGET':str(target)},check=True)
    packed=subprocess.run(['npm','pack','--json','--pack-destination',temp],cwd=ROOT/'typescript',capture_output=True,text=True,check=True)
    metadata=json.loads(packed.stdout[packed.stdout.index('[\n'):])
    tarball=stage/metadata[0]['filename']
    app=stage/'node'
    app.mkdir()
    (app/'package.json').write_text(json.dumps({'private':True,'type':'module','dependencies':{'@hyperroute/sdk':'file:'+str(tarball)}}))
    subprocess.run(['npm','install','--ignore-scripts','--package-lock=false'],cwd=app,check=True,stdout=subprocess.DEVNULL)
    script="import { HyperRoute, VERSION } from '@hyperroute/sdk'; const c = new HyperRoute({ fetch: async () => new Response(JSON.stringify({ready:true,routable:true}),{headers:{'content-type':'application/json'}}) }); if (!(await c.health()).data.routable || !VERSION) throw new Error('Package import failed'); console.log('npm tarball import and client verified');"
    subprocess.run(['node','--input-type=module','-e',script],cwd=app,check=True)
