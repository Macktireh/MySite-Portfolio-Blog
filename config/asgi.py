"""
ASGI config for MySitePortfolio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from dotenv import load_dotenv

load = load_dotenv('../.env')

environment = 'production' if os.getenv('ENVIRONMENT_PRODUCTION') == 'True' else 'development'

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.settings.{environment}')

application = get_asgi_application()
