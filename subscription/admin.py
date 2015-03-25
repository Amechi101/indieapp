from __future__ import unicode_literals

from django.contrib import admin

from subscription.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):

    list_display = ["brand", "user"]
    search_fields = ["user"]


admin.site.register(Subscription, SubscriptionAdmin)

