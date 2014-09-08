from __future__ import unicode_literals

from django.contrib import admin
from product_extend.models import ProductExtend


class ProductExtendAdmin(admin.ModelAdmin):
    list_per_page = 25


admin.site.register(ProductExtend, ProductExtendAdmin)
