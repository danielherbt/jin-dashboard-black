"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os, random, string
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))

# Render Deployment Code
DEBUG = False

# Docker HOST
#ALLOWED_HOSTS = ['localhost', '127.0.0.1','3.213.118.142','salespruebas.main-data.net']
ALLOWED_HOSTS = ['*']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'admin_black.apps.AdminBlackConfig',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'api.base.apps.BaseConfig',
    'api.manage.apps.ManageConfig',
    'api.sales.apps.SalesConfig',
    'api.schoolfees.apps.SchoolfeesConfig',
    'api.docs.apps.DocsConfig',
    'rest_framework',
    'simple_history',
    'django_filters',
    'drf_spectacular',
    "corsheaders",
    "home",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'simple_history.middleware.HistoryRequestMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

SECURE_CROSS_ORIGIN_OPENER_POLICY = None

# Add here your deployment HOSTS
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://localhost:5085', 'http://127.0.0.1:8000', 'http://3.213.118.142:80', 'http://salespruebas.main-data.net:80', 'http://jin-dashboard-black.com:80' ]
ROOT_URLCONF = "core.urls"

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://\w+\.jin-dashboard-black\.com$",
]

HOME_TEMPLATES = os.path.join(BASE_DIR, 'home', 'templates')

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [HOME_TEMPLATES],
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

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DB_ENGINE   = os.getenv('DB_ENGINE'   , None)
DB_USERNAME = os.getenv('DB_USERNAME' , None)
DB_PASS     = os.getenv('DB_PASS'     , None)
DB_HOST     = os.getenv('DB_HOST'     , None)
DB_PORT     = os.getenv('DB_PORT'     , None)
DB_NAME     = os.getenv('DB_NAME'     , None)

if DB_ENGINE and DB_NAME and DB_USERNAME:
    DATABASES = { 
      'default': {
        'ENGINE'  : 'django.db.backends.' + DB_ENGINE, 
        'NAME'    : DB_NAME,
        'USER'    : DB_USERNAME,
        'PASSWORD': DB_PASS,
        'HOST'    : DB_HOST,
        'PORT'    : DB_PORT,
        }, 
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_TZ = True

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    'DEFAULT_SCHEMA_CLASS' :  'drf_spectacular.openapi.AutoSchema' , 
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}


SPECTACULAR_SETTINGS = {
    # General schema metadata. Refer to spec for valid inputs
    # https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#openapi-object
    'TITLE': 'drf-spectacular API Document',
    'DESCRIPTION': 'API ERP-WEB-JIN',
    # Optional: MAY contain "name", "url", "email"
    'CONTACT': {'name': '김성렬', 'url': 'http://www.example.com/support', 'email': 'danielherbt@gmail.com'},
    # Swagger UI를 좀더 편리하게 사용하기위해 기본옵션들을 수정한 값들입니다.
    'SWAGGER_UI_SETTINGS': {
        # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/  <- 여기 들어가면 어떤 옵션들이 더 있는지 알수있습니다.
        'dom_id': '#swagger-ui',  # required(default)
        'layout': 'BaseLayout',  # required(default)
        'deepLinking': True,  # API를 클릭할때 마다 SwaggerUI의 url이 변경됩니다. (특정 API url 공유시 유용하기때문에 True설정을 사용합니다)
        'persistAuthorization': True,  # True 이면 SwaggerUI상 Authorize에 입력된 정보가 새로고침을 하더라도 초기화되지 않습니다.
        'displayOperationId': True,  # True이면 API의 urlId 값을 노출합니다. 대체로 DRF api name둘과 일치하기때문에 api를 찾을때 유용합니다.
        'filter': True,  # True 이면 Swagger UI에서 'Filter by Tag' 검색이 가능합니다
    },
    # Optional: MUST contain "name", MAY contain URL
    'LICENSE': {
        'name': 'MIT License',
        'url': 'https://github.com/KimSoungRyoul/DjangoBackendProgramming/blob/main/LICENSE',
    },
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,  # OAS3 Meta정보 API를 비노출 처리합니다.
     
     # https://www.npmjs.com/package/swagger-ui-dist 해당 링크에서 최신버전을 확인후 취향에 따라 version을 수정해서 사용하세요.
    'SWAGGER_UI_DIST': '//unpkg.com/swagger-ui-dist@3.38.0',  # Swagger UI 버전을 조절할수 있습니다.
    
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#if not DEBUG:
#    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = '/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
