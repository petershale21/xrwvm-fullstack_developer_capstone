#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from django.core.management import execute_from_command_line
from django.contrib.auth import get_user_model


load_dotenv(Path(__file__).parent / 'djangoproj' / '.env')


def create_default_superuser():
    """Create superuser from environment variables if they exist."""
    User = get_user_model()

    # Get credentials from environment variables
    username = os.getenv('DJANGO_SUPERUSER_USERNAME')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')

    if username and password and not User.objects.filter(
        username=username
    ).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"Superuser created: {username}")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')

    try:
        import django
        django.setup()

        # Only attempt superuser creation during specific commands
        if len(sys.argv) > 1 and sys.argv[1] in [
            'runserver',
            'migrate',
            'shell'
        ]:
            try:
                create_default_superuser()
            except django.db.utils.OperationalError:
                # Database isn't ready yet
                pass

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
