import json
import os
import re
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

from openapi_spec_validator import validate
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
api=json.loads((ROOT/'contract/openapi.json').read_text())
validate(api)
assert all(op['x-response-type']!='JsonObject' or op['x-response-mode']=='bytes' for methods in api['paths'].values() for op in methods.values()), 'Every operation needs a named response'
versions={
    'python':tomllib.loads((ROOT/'python/pyproject.toml').read_text())['project']['version'],
    'typescript':json.loads((ROOT/'typescript/package.json').read_text())['version'],
}
for lang,version in versions.items():
    assert re.fullmatch(r'\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?',version)
    path=ROOT/('python/src/hyperroute/__init__.py' if lang=='python' else 'typescript/src/index.ts')
    assert f"'{version}'" in path.read_text(),f'{lang} exported version mismatch'
    transport=ROOT/('python/src/hyperroute/transport.py' if lang=='python' else 'typescript/src/transport.ts')
    assert f'hyperroute-{lang}/{version}' in transport.read_text(),f'{lang} User-Agent version mismatch'
if len(sys.argv)>1:
    lang=sys.argv[1]
    tag=sys.argv[2]
    assert tag==f'{lang}-v{versions[lang]}',f'Tag {tag} does not match {lang} package version'
files=['python/src/hyperroute/types.py','python/src/hyperroute/client.py','typescript/src/types.ts','typescript/src/client.ts','docs/api.md','docs/types.md']
with tempfile.TemporaryDirectory() as temp:
    out=Path(temp)
    for file in files+['contract/openapi.json']:(out/file).parent.mkdir(parents=True,exist_ok=True)
    (out/'contract/openapi.json').write_text(json.dumps(api))
    subprocess.run([sys.executable,str(ROOT/'scripts/generate.py')],env={**os.environ,'HYPERROUTE_GENERATE_ROOT':temp},check=True)
    for file in files:
        assert (ROOT/file).read_bytes()==(out/file).read_bytes(),f'{file} is stale; run scripts/generate.py'
fixtures=json.loads((ROOT/'contract/fixtures.json').read_text())
for key,name in {'recommendation':'LeanRecommendation','full_recommendation':'FullRecommendation','min_recommendation':'MinRecommendation','queued':'RecommendationJob','health':'Health','execution':'ExecutionResult'}.items():
    schema={'$ref':'#/components/schemas/'+name,'components':api['components']}
    Draft202012Validator(schema).validate(fixtures[key])
print(f'OpenAPI, generated files, versions, and {len(fixtures)} fixtures verified')
