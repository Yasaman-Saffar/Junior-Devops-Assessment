# Junior DevOps/SRE Project

## Overview

This is a simple Python HTTP API built with Django REST Framework. It has two endpoints and can run locally or using Docker and Docker Compose.

I used DRF because I was already familiar with it, although Flask might have been a simpler choice for this project.

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python app.py
```

The application runs on port `8000` by default.

You can change the default settings using these environment variables:

- `PORT=8000`
- `APP_VERSION=0.1.0`
- `APP_ENV=local`

## Run with Docker

```bash
docker build -t junior-service:local .
docker run --rm -p 127.0.0.1:8000:8000 junior-service:local
```

## Run with Docker Compose

```bash
docker compose config
docker compose up -d --build
```

To check the endpoints:

```bash
curl -i http://localhost:8000/health
curl -i http://localhost:8000/info
```

Both endpoints should return HTTP 200.

To stop the containers:

```bash
docker compose down
```

## CI

I set up GitHub Actions to automatically run the tests and build the Docker image whenever I push to `main`.

I checked the workflow on GitHub, and it completed successfully.

## Project Status

I completed the API, automated tests, Docker, Docker Compose, and CI stages. I ran the required commands myself and verified the results.

I also completed the incident simulation. I intentionally changed the Docker port mapping, investigated why the application stopped responding, and fixed the issue. I chose to focus on this part because I felt it was more useful for understanding Docker networking and troubleshooting.

I didn't complete the standalone smoke-test script (`scripts/smoke_test.py`) because I ran out of time. I decided to prioritize the incident simulation instead.
