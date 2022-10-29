
from pathlib import Path
import os
from datetime import timedelta
from main.base_app_link import APP_BASE_LINK,GOOGLE_BASE_LINK,FACEBOOK_BASE_LINK

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = "django-insecure-+pc8gqz*8*l#+)%4ukwdo!^pd1z)6n=%wp7j3d0v$tc7b74@z*"

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'corsheaders',
    'accounts',
    'dataTransmission',
    'social_django',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",   
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'frontEnd/build')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"
# ASGI_APPLICATION = 'main.asgi.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "backend/db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    # {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    'OPTIONS': {
            'min_length': 4,
        }
    },
    # {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    # {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontEnd/build/static')
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ALLOWED_HOSTS = ['*']


AUTH_USER_MODEL = 'accounts.Account'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 60
}
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
   'ACCESS_TOKEN_LIFETIME': timedelta(minutes=100),
#    'ROTATE_REFRESH_TOKENS': False,
#    'BLACKLIST_AFTER_ROTATION': False,
#    'UPDATE_LAST_LOGIN': False,
     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'accounts.serializers.AccountCreateSerializer',
        'user': 'accounts.serializers.AccountCreateSerializer',
        'current_user': 'accounts.serializers.AccountCreateSerializer',
        'user_delete': 'accounts.serializers.AccountDeleteSerializer',

        },
    
    'LOGIN_FIELD': 'email',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL':True,
    'USER_CREATE_PASSWORD_RETYPE':True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND':True,
    'SET_PASSWORD_RETYPE':True,
    'LOGOUT_ON_PASSWORD_CHANGE':True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    'PASSWORD_RESET_CONFIRM_URL':'password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'users/activate/{uid}/{token}',
    'SOCIAL_AUTH_TOKEN_STRATEGY':'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS':[APP_BASE_LINK, FACEBOOK_BASE_LINK]
}

## for activation email
DOMAIN = ('localhost:3000') 
SITE_NAME = ('CML') 


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pinhrobot@gmail.com'
EMAIL_HOST_PASSWORD = 'mmuolulyifdpfxjr'
EMAIL_USE_TLS = True


CORS_ALLOW_ALL_ORIGINS = True



AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '95327707786-q4t91qek9l44a5l5r03mofd8qishq35b.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


SOCIAL_AUTH_FACEBOOK_KEY = '825273548516746'
SOCIAL_AUTH_FACEBOOK_SECRET = '6eb56289a272b2622cc6a05829663e74'
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']  # this is extra information about user you can get dusring facebook authentiation process
