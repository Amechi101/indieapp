from __future__ import unicode_literals
from django.contrib import admin


from website.models import Website

class WebsiteAdmin(admin.ModelAdmin):
	list_display = ["name"]
	search_fields = ["id","name"]
	list_per_page = 10

# Register Models below
admin.site.register(Website, WebsiteAdmin)
