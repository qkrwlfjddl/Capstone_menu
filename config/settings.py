"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import pymysql
pymysql.install_as_MySQLdb()
import os 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f$o$-f3u25k8yq3xud@4%=3@@k%t)p$c7o#h#4=18*&_5k5t)&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.compute.amazonaws.com', '127.0.0.1', 'localhost']


# Application definition
#각 폴더의 apps.py에 있는 기능들이 동작 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'storages',
    'shop',
    'cart',
    'coupon',
    'order',
    'users',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [ 
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth', 
                'django.contrib.messages.context_processors.messages', 
                'cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onlineshop',
        'USER' : 'onlineshop',
        'PASSWORD' : 'onlineshop',
        'HOST' : 'onlineshop.csgbkx6pludx.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_unicode_ci',
        },

        
    }
}

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::django-onlineshop-capstone/*"
        }
    ]
}

AWS_ACCESS_KEY_ID = 'AKIAWVWQ4EICMJCQYLS7'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'django-onlineshop-capstone-static'
AWS_S3_CUSTOM_DOMAIN = f's3.{AWS_REGION}.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}'
AWS_S3_FILE_OVERWRITE = False
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = ''

STATIC_URL = f'http://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'



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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', #장고에서 사용하는 기본 모델
    #'allauth.account.auth_backends.AuthenticationBackend', #소셜로그인이 사용하는
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

CART_ID = 'cart_item'

"""STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]"""

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'