#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^webssh$', 'web_ssh.views.webssh', name='webssh'),
	url(r'^webshell$', 'web_ssh.views.index', name='index'),
)
