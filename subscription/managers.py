from __future__ import unicode_literals

from django.db import models 

from subscription.models import Subscription


class SubscriptionManager(models.Manager):

	def subscribe(self, user, brand): 
		return Subscription.objects.create(brand=brand, user=user)

	def unsubscribe(self, user, brand): 
		return Subscription.objects.filter(brand=brand, user=user).delete()

	class Meta:
		unique_together = ("user", "brand")