# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from migraph.urls import urlpatterns as migraph_urls

urlpatterns = [
    url(r'^', include(migraph_urls, namespace='migraph')),
]
