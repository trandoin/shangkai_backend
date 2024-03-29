import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-zzjfseaw#khg4nq$%j*&9z=y$lntt_wzd4y3$i^!*=!#un3d3!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "auth_travel",
    "corsheaders",
    "users",
    "clients",
    "shangkai_app",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "shangkai.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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


WSGI_APPLICATION = "shangkai.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "shangkai_db",
#         "USER": "shangkai",
#         "PASSWORD": "shangkaipass",
#         "HOST": "mysql-dbms.cog4jorwkti6.ap-south-1.rds.amazonaws.com",
#         "PORT": "3306",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "shangkai_shangkai_db",
        "USER": "shangkai_shangkaiUser466",
        "PASSWORD": "sZrGWzBPpU2t@pA",
        "HOST": "212.1.210.139",
        "PORT": "",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "businessinfotrando@gmail.com"
# EMAIL_HOST_PASSWORD = "startup@trando"

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.hostinger.in'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "noreply@trando.in"
# EMAIL_HOST_PASSWORD = "Anoreply@123"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.hostinger.in"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "learning@trando.in"
EMAIL_HOST_PASSWORD = "Learn#46#$(*"


# STATIC_URL = '/root/shangkai_env/shangkai_backend/shangkai/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, "static")
# STATIC_URL = "/root/shangkai_env/shangkai_backend/shangkai/static/"
# STATIC_URL = "/home/ubuntu/travel-env/shangkai_backend/shangkai/static/"


# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
# MEDIA_ROOT = "/root/shangkai_env/shangkai_backend/shangkai/media"
# MEDIA_URL = "/media/"
# STATIC_ROOT = "/root/shangkai_env/shangkai_backend/shangkai/static"
# STATIC_URL = "/static/"

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
# DEFAULT_FILE_STORAGE = 'spread.storage_backends.MediaStorage'

###### AWS S3 ####

# AWS_S3_ACCESS_KEY_ID = 'AKIAV2GHTWDIQTC6MNI4'
# AWS_S3_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'shangkai-s3-bucket'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_SIGNATURE_VERSION = "s3v4"
# AWS_S3_REGION_NAME = "ap-south-1"
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = "public-read"
# AWS_S3_VERIFY = True
# AWS_S3_OBJECT_PARAMETERS = {
#     "CacheControl": "max-age=2592000",
# }

"""Start For Token Authentication """
CORS_ALLOW_CREDENTIALS = True  # to accept cookies via ajax request

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "auth_travel.authentication.SafeJWTAuthentication",
    ),
}


REFRESH_TOKEN_SECRET = "4l7$d1av+8vl1s9175svaazrf8f%$no1*810pz262(k7mnzi9k"

""" END Token Authentication """


CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://shangkai.in",
    "http://shangkai.in",
    "http://partner.shangkai.in",
    "https://partner.shangkai.in",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://shangkai.in",
    "http://shangkai.in",
    "http://partner.shangkai.in",
    "https://partner.shangkai.in",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
