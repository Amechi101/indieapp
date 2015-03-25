from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from . import views

from subscription.views import account_subscribe, unsubscribe, subscribe, SubscriptionListView


urlpatterns = patterns('',

	url(r"^api/subscribe/", views.subscribe),
	url(r"^api/unsubscribe/", UnsubscribeView.as_view()),
	url(r"^subscribed-brands/$", SubscriptionListView.as_view() ),
)

