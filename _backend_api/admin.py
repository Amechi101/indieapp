from __future__ import unicode_literals

from django.contrib import admin
from _backend_api.models import Brand, Product, Location


class BrandAdmin(admin.ModelAdmin):
	list_display = ["brand_name"]
	search_fields = ["brand_name"]
	list_per_page = 25

class ProductAdmin(admin.ModelAdmin):
	list_display = ["product_name"]
	search_fields = ["product_name"]
	list_per_page = 10

class LocationAdmin(admin.ModelAdmin):
	list_display = ["id","contact_type",]
	search_fields = ["contact_type"]
	list_per_page = 10

# Register Models below
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Location, LocationAdmin)
