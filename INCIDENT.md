# Incident Report: Docker Port Mapping Issue

## 1. Error

The application was not responding when I ran:

```bash
curl -i http://localhost:8000/health
```

## 2. Evidence & Investigation

I started troubleshooting independently using the following commands:

- `docker compose logs --tail=30`: No useful error messages were found.
- `docker compose ps`: Showed that host port 8000 was mapped to container port 9999.
- `docker compose config`: Confirmed the incorrect port mapping:

```yaml
target: 9999
published: "8000"
```

I then asked Codex to investigate the issue using this prompt:

> I'm getting an error when I run:
>
> `curl -i http://localhost:8000/health`
>
> The service is supposed to be running through Docker Compose.
>
> Please investigate why the endpoint is not responding.
>
> Check the container status, Docker Compose configuration, port mappings, application logs, and the port the application is listening on.
>
> Don't modify any files or fix the issue yet. I want to understand the problem first.

The agent independently identified the same port-mapping issue.

## 3. Root Cause

Docker Compose forwarded requests from host port `8000` to container port `9999`, while the application was listening on port `8000` inside the container.

The incorrect configuration was:

```yaml
ports:
  - "8000:9999"
```

## 4. Fix

I corrected the port mapping to:

```yaml
ports:
  - "8000:8000"
```

Then recreated the service:

```bash
docker compose up -d --force-recreate
```

## 5. Recovery Verification

The recovery can be verified using:

```bash
docker compose ps
curl -i http://localhost:8000/health
curl -i http://localhost:8000/info
```

Expected result: Both endpoints return HTTP 200 with the expected JSON responses.
