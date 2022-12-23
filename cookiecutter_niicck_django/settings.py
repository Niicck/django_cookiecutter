"""
Django settings for cookiecutter_niicck_django project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

from configurations import Configuration
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR / "cookiecutter_niicck_django"


class Base(Configuration):
    DJANGO_CONFIGURATION = config("DJANGO_CONFIGURATION")

    ROOT_URLCONF = "cookiecutter_niicck_django.base.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "cookiecutter_niicck_django.wsgi.application"

    # Password validation
    # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django

    PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.Argon2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
        "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
        "django.contrib.auth.hashers.ScryptPasswordHasher",
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/4.1/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_TZ = True

    SECRET_KEY = config("SECRET_KEY")

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("POSTGRES_DB"),
            "USER": config("POSTGRES_USER"),
            "PASSWORD": config("POSTGRES_PASSWORD"),
            "HOST": config("POSTGRES_HOST"),
            "PORT": config("POSTGRES_PORT", cast=int),
            "CONN_MAX_AGE": 0,
        }
    }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/

    # When static assets are collected via "collectstatic" command, they will be loaded
    # into this STATIC_ROOT directory.
    # From there, they should be transfered to a proper file server.
    # All other static file settings are handled in their respective Local or Production
    # settings classes.
    STATIC_ROOT = BASE_DIR / "build" / "collect_static"

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    INSTALLED_APPS = [
        # Django
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.postgres",
        # Third Party
        "django_extensions",
        "django_browser_reload",
        # Local
        "cookiecutter_niicck_django.base",
        "cookiecutter_niicck_django.users",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "django_browser_reload.middleware.BrowserReloadMiddleware",
    ]

    DEBUG = config("DEBUG", default=False, cast=bool)

    AUTH_USER_MODEL = "users.User"

    # Django Extensions
    SHELL_PLUS = "ipython"


class Local(Base):
    ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/

    # URLs are for Local development only
    STATIC_URL = "static/"
    MEDIA_URL = "media/"

    # If users upload images during Local development, they will be stored in this
    # directory.
    MEDIA_ROOT = BASE_DIR / "build" / "media"

    # Tell django to serve compiled static files from "build/static" directory during
    # development. (For example, this directory will contain compiled tailwindcss
    # files)
    STATICFILES_DIRS = [
        BASE_DIR / "build" / "static",
    ]


class Test(Base):
    pass


class Production(Base):
    DEBUG = False

    ALLOWED_HOSTS: list = []
