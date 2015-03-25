from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from . import views

from subscription.views import account_subscribe, unsubscribe, subscribe


urlpatterns = patterns('',

	url(r"^api/subscribe/", views.subscribe),
	url(r"^api/unsubscribe/", views.unsubscribe),
	url(r"^subscribed-brands/$", views.account_subscribe ),
)

