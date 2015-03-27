# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse

from django.views.generic import View

from subscription.managers import SubscriptionManager
from subscription.models import Subscription
from _backend_api.models import Brand

import json

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class SubscribeView(LoginRequiredMixin, View):

	def get(self, *args, **kwargs):

		if self.request.user.is_authenticated():
			if self.request.GET.get("ajax"):
				return HttpResponse(json.dumps({ "status" : "ok"} ), content_type="application/json")

			SubscriptionManager().subscribe(brand=get_object_or_404(Brand, brand_name=self.request.GET.get("brand_name") ), user=self.request.user)
			return HttpResponseRedirect("/account/subscribed-brands/?added=")

		return super(SubscribeView, self).get(*args, **kwargs)


class SubscriptionListView(LoginRequiredMixin, View):	
	def get(self, request):
		brands = Subscription.objects.filter(brand=request.user)
		return render_to_response("account/account_features/_user_brands.html", {"brands": brands})
		

class UnsubscribeView(LoginRequiredMixin, View):	
	def get(self, request):
		SubscriptionManager.unsubscribe(brand=get_object_or_404(name=request.GET.get("brand_name"), user=request.user))
		return HttpResponse("ok")
	
	#TODO: switch to POST view	
	def post(self, request):
		SubscriptionManager.unsubscribe(brand=get_object_or_404(name=request.POST.get("brand_name"), user=request.user))
		return HttpResponse("ok")
		

