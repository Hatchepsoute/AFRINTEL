# AFRINTEL connector for OpenCTI

External-import connector that pushes AFRINTEL's monthly STIX 2.1 bundles into
an OpenCTI platform.

```text
victims.md / victims_FR.md
        │  (scripts/afrintel_victims_to_stix.py)
        ▼
stix/<year>/<mm-month>/afrintel_<month>_<year>_opencti.json
        │  (this connector)
        ▼
OpenCTI platform
```

## What it imports

Each monthly bundle contains, per the AFRINTEL STIX modeling rules
(see the repository `CLAUDE.md`, section 19):

- `identity` objects for AFRINTEL, the author, and each victim organization
- `threat-actor` objects for observed actors, groups or leak-site personas
  (never a fictitious "unattributed" actor)
- `incident` objects for each claimed/confirmed case
- `report` objects for monthly and first-half context
- `relationship` objects (`targets`, `attributed-to`, report `object_refs`)

Object IDs are deterministic (`uuid5`, namespaced on the AFRINTEL repo URL),
so the connector can safely resend a bundle it already sent: OpenCTI updates
the existing objects rather than duplicating them. There is no incremental
diff logic to get wrong; the connector just tracks a hash per file in its
OpenCTI connector state to skip bundles that have not changed since the last
run.

## Two data sources

- `github` (default): fetches bundles directly from the public AFRINTEL
  GitHub repository over the GitHub API / raw.githubusercontent.com. No
  checkout needed; works from any OpenCTI deployment.
- `local`: reads bundles from a checkout of this repository mounted into the
  container at `AFRINTEL_REPO_PATH` (default `/repo`). Use this if you run
  the connector next to a local clone that you update yourself.

## Configuration

Copy `config.yml.sample` to `config.yml` and fill in `opencti.url`,
`opencti.token` and a fresh `connector.id` (any UUIDv4), or set the
equivalent environment variables (`OPENCTI_URL`, `OPENCTI_TOKEN`,
`CONNECTOR_ID`, `AFRINTEL_SOURCE`, `CONNECTOR_DURATION_PERIOD`, `AFRINTEL_GITHUB_REPO`, ...) — env vars
take precedence over `config.yml`.

| Variable | Purpose | Default |
|---|---|---|
| `AFRINTEL_SOURCE` | `github` or `local` | `github` |
| `AFRINTEL_GITHUB_REPO` | `owner/repo` to pull from | `Hatchepsoute/AFRINTEL` |
| `AFRINTEL_GITHUB_BRANCH` | branch to read | `main` |
| `AFRINTEL_GITHUB_TOKEN` | optional, raises GitHub API rate limits | unset |
| `AFRINTEL_REPO_PATH` | local checkout path (source=local) | `/repo` |
| `CONNECTOR_DURATION_PERIOD` | ISO 8601 delay between runs | `P1D` |

## Run with Docker

```bash
cd connectors/afrintel
cp config.yml.sample config.yml   # edit opencti.url / opencti.token / connector.id
docker build -t afrintel-connector .
docker run --rm --env-file <(python3 -c "import yaml,sys; c=yaml.safe_load(open('config.yml')); print('\n'.join(f'{k.upper()}={v}' for k,v in {**c['opencti'], **c['connector'], **c['afrintel']}.items()))") afrintel-connector
```

Or, more simply, register it as a service in your existing OpenCTI
`docker-compose.yml` using the `connector-afrintel` block from
`docker-compose.yml` in this folder, then:

```bash
docker compose up -d --build connector-afrintel
```

## Run without Docker

```bash
cd connectors/afrintel/src
pip install -r ../requirements.txt
cp ../config.yml.sample ./config.yml   # edit as needed
python3 main.py
```

## Validation

Run these checks before deployment:

    python3 -m py_compile src/main.py src/afrintel_connector.py
    python3 -m json.tool __metadata__/connector_manifest.json
    docker compose --env-file .env.sample config
    docker build -t afrintel-connector .

The connector uses the OpenCTI scheduler, creates a work for each run and
stores one SHA-256 digest per successfully imported bundle in connector state.

## Notes and limitations

- What was **not** tested: registering the connector against a real,
  running OpenCTI instance. `OpenCTIConnectorHelper.__init__` performs a
  live GraphQL handshake with `opencti.url`/`opencti.token`, which this
  environment has no server to satisfy. Before production use, run it once
  against a real (or local docker-compose) OpenCTI to confirm the
  connector registers and the work/state calls succeed end to end.
- The connector only imports what already exists under `stix/`. Run
  `scripts/afrintel_victims_to_stix.py` first (or via CI) to regenerate
  bundles after editing `victims.md` / `victims_FR.md`.
- It never invents actors, victims or relationships: it is a pure transport
  layer for bundles the existing AFRINTEL pipeline already produced.
