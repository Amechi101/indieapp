from __future__ import unicode_literals

from django.conf.urls import patterns, url

from product_extend.views import ProductView


urlpatterns = patterns('',
    url(r'^all/$', ProductView.as_view(), name='product_list'),
)
