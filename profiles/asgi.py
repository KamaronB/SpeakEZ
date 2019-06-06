"""This file swaps out Djangos HTTP/WSGI request handler for Asyncronous Server Gateway
Interface(ASGI)"""

import os
import django
from channels.routing import get_default_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "speakeasy.settings")
channel_layer = get_default_application()
