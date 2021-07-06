#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for web_ssh project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%-jf*(x32k#fnj3pk^9$-6ln)a@4=tr9t1#utq!h(106#10noi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django.contrib.sessions',
	'django.contrib.staticfiles',
	'web_ssh',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'web_ssh.urls'

WSGI_APPLICATION = 'web_ssh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': "django.db.backends.mysql",
		'NAME':"xxx",
		'USER':"root",
		'HOST':"127.0.0.1",
		'PASSWORD':"xxx",
		'PORT':3306,
		'OPTIONS': {'charset': 'utf8mb4'},
	}
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# pip install IPy -i https://pypi.tuna.tsinghua.edu.cn/simple/
# pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python
# pip install -U cos-python-sdk-v5 -i https://mirrors.tencent.com/pypi/simple/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
