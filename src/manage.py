#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import gettext

gettext.install('fichario')

# if not os.getenv('BASE_MODULE'):
#     print('Running manage.py from console.')
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fichario_django.settings')
#     os.environ.setdefault('BASE_MODULE', '')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fichario.fichario_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
