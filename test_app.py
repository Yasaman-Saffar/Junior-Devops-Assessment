import os
from unittest.mock import patch

from django.test import SimpleTestCase


class EndpointTests(SimpleTestCase):
    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_info(self):
        with patch.dict(os.environ):
            os.environ.pop("APP_VERSION", None)
            os.environ.pop("APP_ENV", None)
            response = self.client.get("/info")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"version": "0.1.0", "environment": "local"})

        with patch.dict(os.environ, APP_VERSION="1.2.3", APP_ENV="staging"):
            response = self.client.get("/info")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {"version": "1.2.3", "environment": "staging"})
