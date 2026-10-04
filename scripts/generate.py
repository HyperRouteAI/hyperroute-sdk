import json
import os
import re
from pathlib import Path

ROOT = Path(os.environ.get('HYPERROUTE_GENERATE_ROOT', Path(__file__).resolve().parents[1]))
api = json.loads((ROOT / 'contract/openapi.json').read_text())


def typename(s, language):
    if '$ref' in s:
        return s['$ref'].rsplit('/', 1)[1]
    if 'anyOf' in s:
        return ' | '.join(typename(x, language) for x in s['anyOf'])
    if 'const' in s:
        return 'Literal[' + repr(s['const']) + ']' if language == 'py' else json.dumps(s['const'])
    if 'enum' in s:
        values = ', '.join(repr(v) for v in s['enum']) if language == 'py' else ' | '.join(json.dumps(v) for v in s['enum'])
        return 'Literal[' + values + ']' if language == 'py' else values
    t = s.get('type')
    if t == 'array':
        inner = typename(s.get('items', {}), language)
        return f'list[{inner}]' if language == 'py' else f'Array<{inner}>'
    if t == 'object':
        extra = s.get('additionalProperties')
        if isinstance(extra, dict):
            inner = typename(extra, language)
            return f'dict[str, {inner}]' if language == 'py' else f'Record<string, {inner}>'
        return 'JsonObject'
    return ({'string':'str','integer':'int','number':'float','boolean':'bool','null':'None'} if language == 'py' else {'string':'string','integer':'number','number':'number','boolean':'boolean','null':'null'}).get(t, 'Any' if language == 'py' else 'unknown')


def camel(name):
    return re.sub(r'_([a-z])', lambda m: m[1].upper(), name)


py = ['from __future__ import annotations', 'from typing import Any, Literal, NotRequired, TypedDict, TypeAlias, Union', '', 'JsonObject = dict[str, Any]', '']
ts = ['export type JsonObject = Record<string, unknown>;', '']
for name, s in api['components']['schemas'].items():
    if name == 'JsonObject':
        continue
    if 'anyOf' in s:
        py.append(f'{name}: TypeAlias = Union[' + ', '.join(repr(typename(x, 'py')) for x in s['anyOf']) + ']')
        ts.append(f'export type {name} = ' + typename(s, 'ts') + ';')
        continue
    py.append(f'class {name}(TypedDict):')
    ts.append(f'export interface {name} {{')
    for key, field in s.get('properties', {}).items():
        required = key in s.get('required', [])
        ptype, ttype = typename(field,'py'), typename(field,'ts')
        py.append(f'    {key}: {ptype if required else "NotRequired[" + ptype + "]"}')
        ts.append(f'  {key}{"" if required else "?"}: {ttype};')
    if not s.get('properties'):
        py.append('    pass')
    py.append('')
    ts.extend(['}', ''])
(ROOT/'python/src/hyperroute/types.py').write_text('\n'.join(py)+'\n')
(ROOT/'typescript/src/types.ts').write_text('\n'.join(ts)+'\n')

sync = ['from __future__ import annotations','from typing import Any, overload','from urllib.parse import quote','from .transport import SyncTransport, AsyncTransport, ApiResponse, RequestOptions','from .types import *','', 'class HyperRoute(SyncTransport):']
async_lines = ['class AsyncHyperRoute(AsyncTransport):']
tslines = ['import { Transport, type ApiResponse, type RequestOptions } from "./transport.js";', 'import type * as T from "./types.js";', '', 'export class HyperRoute extends Transport {']
docs = ['# API reference', '', 'Python methods use snake_case; TypeScript methods use camelCase. Methods return an', '`ApiResponse` with `data`, `status_code` / `statusCode`, and response `headers`.', 'Python accepts request options as keyword arguments; TypeScript takes a final options object.', 'Body parameters are typed request objects. Path parameters precede the body or query object.', '', '| Python | TypeScript | HTTP | Body | Response data |', '|---|---|---|---|---|']
for path, methods in api['paths'].items():
    for method, op in methods.items():
        name = op['operationId']
        body = op.get('requestBody',{}).get('content',{}).get('application/json',{}).get('schema',{}).get('$ref','').rsplit('/',1)[-1]
        params = op.get('parameters',[])
        paths = [p for p in params if p['in']=='path']
        queries = [p for p in params if p['in']=='query']
        response = op['x-response-type']
        mode = op['x-response-mode']
        p_response = 'bytes' if mode=='bytes' else response+' | str' if mode=='auto' else response
        t_response = 'Uint8Array' if mode=='bytes' else 'T.'+response+' | string' if mode=='auto' else 'T.'+response
        p_args = ['self']+[p['name']+': str' for p in paths]
        t_args = [p['name']+': string' for p in paths]
        if body:
            p_args.append('body: '+body)
            t_args.append('body: T.'+body)
        if queries:
            qname = ''.join(x.title() for x in name.split('_'))+'Query'
            p_required = [p for p in queries if p['required']]
            qp = ['class '+qname+'(TypedDict):']
            qt = ['export interface '+qname+' {']
            for p in queries:
                ptype,ttype=typename(p['schema'],'py'),typename(p['schema'],'ts')
                qp.append(f'    {p["name"]}: {ptype if p["required"] else "NotRequired["+ptype+"]"}')
                qt.append(f'  {p["name"]}{"" if p["required"] else "?"}: {ttype};')
            with (ROOT/'python/src/hyperroute/types.py').open('a') as f:f.write('\n'+'\n'.join(qp)+'\n')
            with (ROOT/'typescript/src/types.ts').open('a') as f:f.write('\n'+'\n'.join(qt)+'\n}\n')
            p_args.append('query: '+qname+('' if p_required else ' | None = None'))
            t_args.append('query: T.'+qname+('' if p_required else ' = {}'))
        p_args.extend(['*', 'options: RequestOptions | None = None'])
        t_args.append('options: RequestOptions = {}')
        ppath = repr(path)
        tpath = json.dumps(path)
        for p in paths:
            ppath += f'.replace("{{{p["name"]}}}", quote({p["name"]}, safe=""))'
            tpath += f'.replace("{{{p["name"]}}}", encodeURIComponent({p["name"]}))'
        if name == 'recommend':
            p_args[1] = 'body: RecommendRequest | TextRecommendRequest | FullRecommendRequest | MinRecommendRequest | LeanRecommendRequest'
        call = f'self._request({method.upper()!r}, {ppath}, body={"body" if body else "None"}, query={"query" if queries else "None"}, mode={mode!r}, options=options)'
        if name == 'recommend':
            for req, res in [('TextRecommendRequest', 'str'), ('FullRecommendRequest', 'FullRecommendation'), ('MinRecommendRequest', 'MinRecommendation'), ('LeanRecommendRequest', 'LeanRecommendation'), ('RecommendRequest', 'Recommendation | str')]:
                for dest, prefix in [(sync, ''), (async_lines, 'async ')]:
                    dest.extend(['    @overload', f'    {prefix}def recommend(self, body: {req}, *, options: RequestOptions | None = None) -> ApiResponse[{res}]: ...', ''])
                tsres = 'string' if res == 'str' else 'T.Recommendation | string' if res == 'Recommendation | str' else 'T.' + res
                tslines.append(f'  recommend(body: T.{req}, options?: RequestOptions): Promise<ApiResponse<{tsres}>>;')
        for dest, prefix, awaiter in [(sync,'',''),(async_lines,'async ','await ')]:
            dest.extend([f'    {prefix}def {name}({", ".join(p_args)}) -> ApiResponse[{p_response}]:',f'        return {awaiter}{call}',''])
        tslines.extend([f'  {camel(name)}({", ".join(t_args)}): Promise<ApiResponse<{t_response}>> {{', f'    return this.request({json.dumps(method.upper())}, {tpath}, {"body" if body else "undefined"}, {"query" if queries else "undefined"}, {json.dumps(mode)}, options);','  }',''])
        docs.append(f'| `{name}` | `{camel(name)}` | `{method.upper()} {path}` | {"`"+body+"`" if body else "—"} | `{p_response}` |')
(ROOT/'python/src/hyperroute/client.py').write_text('\n'.join(sync+['']+async_lines).rstrip()+'\n')
(ROOT/'typescript/src/client.ts').write_text('\n'.join(tslines+['}'])+'\n')
(ROOT/'docs/api.md').write_text('\n'.join(docs)+'\n')

schema_docs = ['# Data types', '', 'Generated from the [OpenAPI contract](../contract/openapi.json). Python exports these types from', '`hyperroute.types`; TypeScript exports them from `@hyperroute/sdk`. Python values are ordinary', 'dictionaries described by `TypedDict`. TypeScript values are ordinary objects described by interfaces.', 'Optional means a field may be absent. Nullable means it may contain JSON null. Unknown additional', 'response fields are preserved at runtime. See [recommendations](recommendations.md) for score semantics.', '']
for name, s in api['components']['schemas'].items():
    schema_docs.extend(['## '+name, '', '| Field | Type | Required | Description |', '|---|---|---|---|'])
    for key, field in s.get('properties',{}).items():
        t = typename(field,'ts').replace('|','\\|')
        schema_docs.append(f'| `{key}` | `{t}` | {"Yes" if key in s.get("required",[]) else "No"} | {field.get("description","")} |')
    if 'anyOf' in s:
        schema_docs.append('| — | ' + ' or '.join('`' + typename(x,'ts') + '`' for x in s['anyOf']) + ' | — | Projection-specific union. |')
    elif not s.get('properties'):
        schema_docs.append('| — | Open JSON object | — | Additional fields are preserved. |')
    schema_docs.append('')
(ROOT/'docs/types.md').write_text('\n'.join(schema_docs).rstrip()+'\n')
