# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.utils.decorators import method_decorator

from django.views.generic import View, ListView

from subscription.managers import SubscriptionManager
from subscription.models import Subscription
from _backend_api.models import Brand

import json

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class SubscribeView(LoginRequiredMixin, View):
	def get(self, request):
		if self.request.user.is_authenticated():
			if self.request.GET.get("ajax"):
				if (Subscription.objects.filter(user=request.user, brand=get_object_or_404(Brand, brand_name=self.request.GET.get("brand_name") ))):
					return HttpResponse(json.dumps({ "status" : "exists"} ), content_type="application/json")
                SubscriptionManager().subscribe(brand=get_object_or_404(Brand, brand_name=self.request.GET.get("brand_name") ), user=self.request.user)
                return HttpResponse(json.dumps({ "status" : "ok"} ), content_type="application/json")


class UnsubscribeView(LoginRequiredMixin, View):	
	def get(self, request):
		SubscriptionManager().unsubscribe(brand=get_object_or_404(Brand, brand_name=self.request.GET.get("brand_name") ), user=request.user)
		return HttpResponse(json.dumps({ "status" : "ok"} ), content_type="application/json")
	
	def post(self, request):
		SubscriptionManager().unsubscribe(brand=get_object_or_404(name=request.POST.get("brand_name"), user=request.user))
		return HttpResponse(json.dumps({ "status" : "ok"} ), content_type="application/json")
		

class SubscriptionListView(LoginRequiredMixin, ListView):	
	
	template_name = "account/account_features/_user_brands.html"
	context_object_name = 'subscribed'
	

	def get(self, request, *args, **kwargs):
		self.brands = Subscription.objects.filter(user=request.user)

		return super(SubscriptionListView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		ctx = super(SubscriptionListView, self).get_context_data(**kwargs)
		
		ctx['brands'] = self.brands

		return ctx

	def get_queryset(self, **kwargs):
		return self.brands

