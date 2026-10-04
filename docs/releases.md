# Compatibility and releases

Python and TypeScript packages use independent Semantic Versions. Before 1.0, breaking changes
increment the minor version and include migration instructions; compatible fixes increment the
patch version. After 1.0, breaking changes increment the major version. Published versions are
immutable.

The [OpenAPI contract](../contract/openapi.json) describes the supported HTTP API. Its version
identifies the contract revision. The API currently uses unversioned HTTP paths. Supported
runtimes are Python 3.11–3.14 and Node.js 22/24.

## Packages

| Language | Registry | Package | Release tag |
|---|---|---|---|
| Python | PyPI | `hyperroute-sdk` | `python-v<VERSION>` |
| TypeScript / JavaScript | npm | `@hyperroute/sdk` | `typescript-v<VERSION>` |

Release workflows check package versions, validate the contract, run tests, and build distributable
packages before publication. Tags must match the package and exported client versions.

## Compatibility

Request and response types, required fields, nullability, projections, and transport behavior are
part of the public contract. Changes are recorded in the [changelog](../CHANGELOG.md). Breaking
changes include migration instructions.

Additional response fields are preserved at runtime. Third-party tool output is represented as an
open payload; the SDK does not impose a schema on a tool's own result.
