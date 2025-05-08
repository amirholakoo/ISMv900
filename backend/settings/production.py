from .base import *

DEBUG = False
ALLOWED_HOSTS = ["your-production-domain.com"]

# Use PostgreSQL in production
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ISM",
        "USER": "postgres",
        "PASSWORD": "62443444",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# If you're in production, you might also need:
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
