from pathlib import Path
from dotenv import load_dotenv
import os
from os import environ

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get("SECRET_KEY"),

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']


# APP CONFIGURATION
DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.sites",
)
THIRD_PARTY_APPS = (
    "rest_framework",
    "django_filters",
    "corsheaders",
    "gunicorn",
    "whitenoise",
    "import_export",
    "rest_framework_swagger",
    "drf_yasg",
    "storages",
)
# Apps specific for this project go here.
LOCAL_APPS = (
    "accounts",
    "settings",
    "billing",
    "message",
)
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [
            BASE_DIR / "templates/",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# CACHING CONFIGURATION
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": environ.get("REDIS_URL"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1


# --- S3 storages ---
AWS_ACCESS_KEY_ID = environ.get("AWS_ACCESS_KEY_ID"),
AWS_SECRET_ACCESS_KEY = environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = environ.get("AWS_S3_REGION_NAME")
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_SIGNATURE_VERSION = "s3v4"

STATICFILES_STORAGE = 'core.settings.storage_backends.StaticStorage'
DEFAULT_FILE_STORAGE = 'core.settings.storage_backends.MediaStorage'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = []
MEDIA_ROOT = 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTH USER MODEL CONFIGURATION
AUTH_USER_MODEL = "accounts.User"
# END AUTH USER MODEL CONFIGURATION

APPEND_SLASH = False


# OTP CONFIGURATION
OTP_CODE_LENGTH = int(os.getenv("OTP_CODE_LENGTH", default="4"))
OTP_TTL = int(os.getenv("OTP_TTL", default="120"))
# END OTP CONFIGURATION

# JWT SETIINGS
JWT_SECRET = "jango-insecure-_#2hxi#d@7!6bg((p@tmy-)#y3i_ad=n!pm4@_h2c60+1m9gty"
ACCESS_TTL = int(os.getenv("ACCESS_TTL", default="7"))  # days
REFRESH_TTL = int(os.getenv("REFRESH_TTL", default="15"))  # days
# END JWT SETTINGS


# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("accounts.backends.jwt_auth.JWTAuthentication",),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    "DEFAULT_THROTTLE_RATES": {"otp": os.getenv("OTP_THROTTLE_RATE", default="10/min"), },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
# END REST FRAMEWORK CONFIGURATION


# ZARRINPAL CONFIGURATION
ZARRINPAL_URL="https://api.zarinpal.com/pg/"
ZARRINPAL_MERCHANT_ID = "38541d6c-9eb6-45f9-830e-7248be500437"
ZP_API_REQUEST = "https://www.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = "https://www.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/"
ZARIN_CALL_BACK = 'https://api.fiko.app/api/v1/billing/payment-verify/'
# END ZARRINPAL CONFIGURATION



# CORSHEADERS CONFIGURATION
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:3000',
    'https://app.fiko.net',
    'https://api.fiko.net',
    'https://fiko.net',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000'
]
# END CORSHEADERS CONFIGURATION
