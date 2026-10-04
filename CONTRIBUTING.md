# Contributing

The public HTTP contract lives in `contract/openapi.json`. Update it before regenerating request
types, client methods, and the API reference with `python scripts/generate.py`.

```sh
python3 -m venv .venv
.venv/bin/pip install -e './python[dev]'
.venv/bin/python scripts/check.py
.venv/bin/python -m pytest python/tests
.venv/bin/mypy python/tests/typecheck.py
.venv/bin/python -m build python
npm --prefix typescript ci
npm --prefix typescript test
npm pack ./typescript --dry-run
```

Keep supported clients in sync for API changes. Add shared fixtures for changed response shapes,
transport tests for behavioral changes, and update affected examples and release notes.

Do not commit credentials or local environment files.

See [container checks](docs/testing.md) to install distributions and run examples in disposable containers.
