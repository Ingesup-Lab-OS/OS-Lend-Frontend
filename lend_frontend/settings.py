"""
Django settings for vmlocation project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

HEAT_TEMPLATE_NAME = 'OS-Lend-Templates'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gp^8r^z-#21cv)#b%o-(td&9$iy@ao4((m$*-&!!%^vq0r^azn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'lend_frontend',
    'django.contrib.staticfiles' 
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lend_frontend.urls'

WSGI_APPLICATION = 'lend_frontend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),
)

STATICFILES_DIRS = (
    os.path.join(
        os.path.dirname(__file__),
        'static',
    ),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

OS_PARAMS = {
    'auth_url': 'http://10.31.92.131:5000/v2.0',
    'tenant_name': 'OS-Lend',
    'username': 'a.cavat',
    'password': 'CecoojEg8'
}

SHORT_TEMPLATE_FOLDER = 'OS-Lend-Templates/heat'
FULL_TEMPLATE_FOLDER = BASE_DIR+ '/'+SHORT_TEMPLATE_FOLDER

SUBNET_ID = '00e35c36-b081-4733-842d-5a335fab5ae3'
NET_ID = '84fe7f1a-880d-4c4b-a34c-dd9e34911229'
FLOATING_ID = '53d84562-4718-41f2-9989-f848ecbd1aa6'
