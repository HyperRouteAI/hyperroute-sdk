# Container examples

The container check installs the built Python wheel or npm tarball in a disposable container and
runs the matching language's examples. Source packages and host dependencies are not installed
in the containers. Package files and example scripts are mounted read-only.

Requires Docker on Linux, a built Python wheel in `python/dist`, and an npm tarball in `typescript`.
Build them from the repository root:

```sh
.venv/bin/python -m build python
npm pack ./typescript --pack-destination ./typescript
```

Run one language's examples against a local fixture:

```sh
.venv/bin/python scripts/check_docker_examples.py --language python
.venv/bin/python scripts/check_docker_examples.py --language typescript
```

Run read-only examples against `https://hyperroute.io`:

```sh
.venv/bin/python scripts/check_docker_examples.py --language python --live
.venv/bin/python scripts/check_docker_examples.py --language typescript --live
```

Live mode excludes execution and feedback and supplies no authentication token. Fixture mode runs
all examples using synthetic responses. Output is saved under `test-results/docker/`, which is
excluded from version control. Containers are removed after each run. The local fixture is
reached through Docker host networking.
