"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@emsiaz&$@yzdvzs(hz4c9x6tdql7tn(0p#=^t77#r6welpp$5'

# SECURITY WARNING: don't run with debug turned on in production!

if "DEBUG" not in os.environ:
    DEBUG   = True
else:
    DEBUG = os.environ["DEBUG"]

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "diy.apps.DiyConfig",
    "diy.templatetags.param_change",
    "users.apps.UsersConfig",

    "django_summernote",
    "django_cleanup",

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.sites',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

AUTH_USER_MODEL = 'users.CustomUser'
ACCOUNT_FORMS   = { "signup":"users.forms.SignupForm"}


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

ACCOUNT_AUTHENTICATION_METHOD   = "email"
ACCOUNT_USERNAME_REQUIRED       = "False"
ACCOUNT_EMAIL_VARIFICATION      = "mandatory"
ACCOUNT_EMAIL_REQUIRED          = True
EMAIL_BACKEND                   = "django.core.mail.backends.console.EmailBackend"

SITE_ID                         = 1
LOGIN_REDIRECT_URL              = '/'
ACCOUNT_LOGOUT_REDIRECT_URL     = '/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'users.middleware.calc.Totalling',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "templates", BASE_DIR / "templates" / "allauth" ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

if DEBUG:
    STATICFILES_DIRS = [ BASE_DIR / "static" ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL   = "/media/"

if DEBUG:
    MEDIA_ROOT  = BASE_DIR / "media"



#TODO: DjangoSummernoteを実装する。

# https://github.com/summernote/django-summernote
SUMMERNOTE_CONFIG = {
    'summernote': {
        'width': '100%',
        'height': '480',
    }
}

# bleach
# HTMLField
ALLOWED_TAGS = [
    'a', 'div', 'p', 'span', 'img', 'em', 'i', 'li', 'ol', 'ul', 'strong', 'br',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'table', 'tbody', 'thead', 'tr', 'td',
    'abbr', 'acronym', 'b', 'blockquote', 'code', 'strike', 'u', 'sup', 'sub','font'
]
ATTRIBUTES = {
    '*': ['style', 'align', 'title', ],
    'a': ['href', ],
    'img': ['src', ],
}


if DEBUG:
    from .local_settings import *

if not DEBUG:

    # ALLOWED_HOSTSにホスト名)を入力
    ALLOWED_HOSTS = [ os.environ["HOST_NAME"] ]

    # 静的ファイル配信ミドルウェア、whitenoiseを使用。※ 順番不一致だと動かないため下記をそのままコピーする。
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',

        'users.middleware.calc.Totalling',

        ]

    # DBを使用する場合は下記を入力する。
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ["DB_NAME"],
                'USER': os.environ["DB_USER"],
                'PASSWORD': os.environ["DB_PASS"],
                'HOST': os.environ["DB_HOST"],
                'PORT': '5432',
                }
            }

    #HerokuPostgresの接続方法(SSL使用、接続の有効時間は600秒)
    import dj_database_url
    db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'].update(db_from_env)

    # 静的ファイル(static)の存在場所を指定する。
    STATIC_ROOT = BASE_DIR / 'static'

    SECRET_KEY = os.environ["SECRET_KEY"]

    STRIPE_API_KEY          = os.environ["STRIPE_API_KEY"]
    STRIPE_PUBLISHABLE_KEY  = os.environ["STRIPE_PUBLISHABLE_KEY"]
    STRIPE_PRICE_ID         = os.environ["STRIPE_PRICE_ID"]

    
    #INSTALLED_APPSにcloudinaryの追加
    INSTALLED_APPS.append('cloudinary')
    INSTALLED_APPS.append('cloudinary_storage')

    #cloudinaryの設定
    CLOUDINARY_STORAGE = { 
            'CLOUD_NAME': os.environ['CLOUD_NAME'], 
            'API_KEY'   : os.environ['API_KEY'], 
            'API_SECRET': os.environ['API_SECRET'],
            "SECURE"    : True,
            }

    #これで全てのファイルがアップロード可能(上限20MB)
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'

