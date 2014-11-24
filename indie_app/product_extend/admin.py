from __future__ import unicode_literals

from django.contrib import admin
from product_extend.models import Product


class ProductAdmin(admin.ModelAdmin):
	list_display = ["name"]
	search_fields = ["name"]
	list_per_page = 25


admin.site.register(Product, ProductAdmin)
