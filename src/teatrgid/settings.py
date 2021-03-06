"""
Django settings for teatrgid project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o@z%4)^%w!31@u%wg*h=ky(g*4+a7xui^_n%@$6$zv7%=@3ygr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# geo
URL_IPGEOBASE = "http://ipgeobase.ru:7020/geo?ip="
KEY_CITY_SESSION = "city_user"

# Красноярск - 37.112.199.0
# Новосибирск - 37.194.20.170
# Москва - 5.62.157.0
# Санкт-Петербург - 5.188.0.0
TEST_IP = "37.194.20.170"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compressor',
    'singlemodeladmin',
    'adminsortable2',
    'easy_thumbnails',

    'teatrgid.custom_user',
    'teatrgid.general_information',
    'teatrgid.performances',
    'teatrgid.theaters',
    'teatrgid.persons',
    'teatrgid.thirdparty_resources',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'teatrgid.general_information.middleware.CityMiddleware'
]

ROOT_URLCONF = 'teatrgid.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, '../frontend/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'teatrgid.general_information.context_processors.name_city_user',
                'teatrgid.general_information.context_processors.list_city',
            ],
        },
    },
]

WSGI_APPLICATION = 'teatrgid.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'teatrgid_db',
        'USER': 'teatrgid_user',
        'PASSWORD': '0XIgP4lL35sgk6Rm',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# custom user
AUTH_USER_MODEL = 'custom_user.User'


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Novosibirsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../frontend/static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, '../var/static')

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../var/media')
MEDIA_URL = '/media/'


# compressor settings

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = not DEBUG
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_PRECOMPILERS = (
    ['text/x-sass', 'sassc --style compressed {infile} {outfile}'],
)
