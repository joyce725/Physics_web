#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description:

"""

from django.conf.urls import patterns, url
from physics import views

urlpatterns = patterns('',
    url(r'^register', views.register),
    url(r'^login', views.login),
)