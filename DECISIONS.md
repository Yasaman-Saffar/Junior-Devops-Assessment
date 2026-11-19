# Decisions & AI Usage

## 1. API Framework

I chose Django REST Framework (DRF) because I was already familiar with it. Although Flask might have been a lighter choice for such a small API, familiarity with DRF helped me work more efficiently.

## 2. AI Agent Usage & Verification

I used Codex throughout most stages for implementation and troubleshooting. I independently executed the verification commands from the assignment and checked the results.

During API testing, `python -m pytest -q` initially failed with:

`django.core.exceptions.ImproperlyConfigured: Requested setting DATABASES, but settings are not configured.`

I asked Codex to investigate the root cause, fix the configuration, and explain its changes without committing anything.

I also questioned why its earlier tests had passed. Codex clarified that it had used Django's test runner (`python -m django test --settings=settings`) and live HTTP checks, but had not initially run pytest.

The fix added `pytest.ini` to configure Django settings and updated the testing dependencies. The subsequent pytest run passed both tests.

## 3. Docker, Compose & CI

I followed the assignment instructions for Docker and Docker Compose and independently verified that the required checks passed.

For CI, my initial GitHub push was rejected because the fine-grained personal access token lacked the necessary workflow modification permission. I used a classic Personal Access Token (PAT) with `repo` and `workflow` scopes to authorize pushing the GitHub Actions workflow.

## 4. Incident & Recovery

I chose to simulate an incorrect Docker port mapping because it demonstrates how container networking and host-to-container port forwarding work.

I used the AI agent to investigate the connection failure, while reviewing the diagnostic commands and their results to understand the root cause before applying the fix.
