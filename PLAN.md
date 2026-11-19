# Minimal HTTP service plan

1. Build two JSON-only GET views with Django REST Framework (DRF) and pin dependencies in `requirements.txt`. `GET /health` returns HTTP 200 with `{"status":"ok"}`. `GET /info` returns HTTP 200 with `version` and `environment` from `APP_VERSION` and `APP_ENV`, defaulting to `0.1.0` and `local`. Read `PORT` at startup and default to `8000`. Keep the service stateless and database-free.
2. Run locally and use `curl -i` to verify both status codes and JSON bodies. Add one lightweight automated test per endpoint, covering health plus default and overridden metadata.
3. Add a `Dockerfile` and `.dockerignore`. Bind to `0.0.0.0` in the container, publish port `8000`, and repeat the HTTP checks with environment overrides. Then add a single-service `compose.yaml` and verify it with `docker compose up --build` and the same checks.
4. Commit and push each verified milestone. Record run commands and any unfinished work in `README.md`. If time permits, run the tests on push with GitHub Actions, then add an image build, a smoke test, and the assignment’s failure-and-recovery exercise.

DRF adds dependencies and settings for two routes. Its request handling and API test client fit the preferred framework. Django’s development server is sufficient for this local and container exercise. `/health` checks that the process can serve HTTP, which is enough for a service with no external dependencies.
