from __future__ import unicode_literals

from django.contrib import admin
from _backend_api.models import Product
from _backend_api.models import Website


class ProductAdmin(admin.ModelAdmin):
	list_display = ["product_name"]
	search_fields = ["product_name"]
	list_per_page = 25


class WebsiteAdmin(admin.ModelAdmin):
	list_display = ["name"]
	search_fields = ["id","name"]
	list_per_page = 10

# Register Models below
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Product, ProductAdmin)
