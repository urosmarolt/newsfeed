"""
Django settings for aggregator project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DJANGO_MODE = os.getenv('DJANGO_MODE', "Production").lower()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if DJANGO_MODE == 'local':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

INTERNAL_IPS = ('127.0.0.1',)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'newsfeed',
    'constance',
    'sitetree',
]

if DJANGO_MODE == 'local':
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DJANGO_MODE == 'local':
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = 'aggregator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'aggregator', 'templates')],
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

WSGI_APPLICATION = 'aggregator.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if DJANGO_MODE == 'local':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'aggregator',
            'USER': 'postgres',
            'PASSWORD': 'postgres123',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
elif DJANGO_MODE == 'staging':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST', '127.0.0.1'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }
elif DJANGO_MODE == 'production':
    import dj_database_url
    #Handles DATABASE_URL env table
    DATABASES = {
        'default': dj_database_url.config()
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'aggregator', 'static'),
)

#twitter auth
#twitter tokens and secrets
OAUTH_TOKEN='2786833384-XzJAtzGcPLsNORDn5yVDOCCkuBWK46SCL3KJvTA'
OAUTH_SECRET='UvLP3J4xc59yXKmOwUB2v8d2vhvpbKGivjb6JxOxyAn32'
CONSUMER_KEY='N6rD2I7TBTg4ceYDJ3kNPWPuW'
CONSUMER_SECRET='ahPlFMiORJRv04tY8el5gxmgCtrPUUNo41dLnfdpt5DT1KMTp5'

#Constance dynamic settings
#CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_BACKEND = 'constance.backends.redisd.RedisBackend'

if DJANGO_MODE == 'local' or DJANGO_MODE == 'staging':
    CONSTANCE_REDIS_CONNECTION = {
        'host': 'localhost',
        'port': 6379,
        'db': 0,
    }
elif DJANGO_MODE == 'production':
    from urllib.parse import urlparse

    redis_url = urlparse(os.getenv('REDIS_URL'))

    CONSTANCE_REDIS_CONNECTION = {
        'host': redis_url.hostname,
        'port': redis_url.port,
        'db': 0,
        'password': redis_url.password,
    }

CONSTANCE_ADDITIONAL_FIELDS = {
    'yes_no_null_select': [
        'django.forms.fields.ChoiceField',
        {
            'widget': 'django.forms.Select',
            'choices': ((None, "-----"), ("yes", "Yes"), ("no", "No"))
        }
    ],
    'email': ('django.forms.fields.EmailField',),
}

CONSTANCE_CONFIG = {
    'SITE_TITLE': ("FakeNew5!", 'Site title'),
    'TWEETER_KEYWORDS': ("#Tweeter", 'Tweeter search keywords'),
    'EVENTREGISTRY_QUERY': ("Fake News", 'Eventregistry search keywords'),
}
