from __future__ import unicode_literals

from django.conf.urls import patterns, url
from product_extend.views import ProductView


urlpatterns = patterns('',
	url(r'^(?P<website_slug>[\w]+)$', ProductView.as_view(), name='product_list'),
)


