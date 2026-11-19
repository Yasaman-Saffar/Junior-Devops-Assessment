import os

from django.core.management import execute_from_command_line


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    try:
        port = int(os.getenv("PORT") or "8000")
    except ValueError:
        raise SystemExit("PORT must be an integer from 1 to 65535.") from None
    if not 1 <= port <= 65535:
        raise SystemExit("PORT must be an integer from 1 to 65535.")

    execute_from_command_line(["app.py", "runserver", f"0.0.0.0:{port}", "--noreload"])


if __name__ == "__main__":
    main()
