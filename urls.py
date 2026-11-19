import os

from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})


@api_view(["GET"])
def info(request):
    return Response({
        "version": os.getenv("APP_VERSION") or "0.1.0",
        "environment": os.getenv("APP_ENV") or "local",
    })


urlpatterns = [
    path("health", health),
    path("info", info),
]
