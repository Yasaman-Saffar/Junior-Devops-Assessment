# Minimal HTTP service

A stateless Python HTTP API built with Django REST Framework for the Junior DevOps/SRE assessment. It exposes two JSON endpoints and runs locally, in Docker, or through Docker Compose.

## Run locally and test

From the repository root, use Python 3.14 and install the service and test dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python app.py
```

The two tests use Django's in-process client, with settings loaded by pytest-django from `pytest.ini`. They need no running server or database. The service listens on `0.0.0.0:8000` by default. Set `PORT`, `APP_VERSION`, and `APP_ENV` before startup to override `8000`, `0.1.0`, and `local`.

## Run in Docker

Choose one launch method at a time because each uses host port 8000.

```bash
docker build -t junior-service:local .
docker run --rm -p 127.0.0.1:8000:8000 junior-service:local
```

Or use Compose, which builds the same Dockerfile and sets `APP_ENV=compose`.

```bash
docker compose config
docker compose up --build -d
```

From a separate terminal, check the running service.

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/info
```

Both should return HTTP 200. Health returns `{"status":"ok"}`. Info returns `{"version":"0.1.0","environment":"local"}` by default, or `"environment":"compose"` under Compose. Stop the foreground process with Ctrl+C or stop Compose with `docker compose down`.

## CI

[The CI workflow](.github/workflows/ci.yml) runs on pushes to `main`. An Ubuntu runner checks out the repository with read-only access, sets up Python 3.14, installs requirements, runs pytest, and builds the Docker image. In GitHub, open **Actions → CI**, select the run for your commit, and check the **Run tests** and **Build Docker image** steps.

## Assignment status

| Guide steps | Status |
| --- | --- |
| 0–1 · Setup and plan | Environment checks are recorded in [SETUP.md](SETUP.md), and the implementation plan is in [PLAN.md](PLAN.md). |
| 2 · API and tests | Both endpoints were verified over HTTP locally. Both pytest tests passed. |
| 3–4 · Docker and Compose | The image built and both endpoints responded with default and overridden settings in Docker. Compose configuration passed validation and both endpoints returned HTTP 200 through host port 8000. |
| 5 · GitHub Actions | Workflow implemented. A successful hosted run is unverified. |
| 6 · Smoke test | Live HTTP checks were performed. The guide's standalone smoke-test script is missing. |
| 7 · Failure and recovery | [INCIDENT.md](INCIDENT.md) records the port mismatch and fix. After recovery, Compose showed `8000:8000` and both endpoints returned HTTP 200 with the expected JSON. |
| 8 · Handoff | This README and [DECISIONS.md](DECISIONS.md) are present locally. Publication of the final handoff files and public repository visibility are unverified. |

The service uses Django's development server for the local and container exercise.
