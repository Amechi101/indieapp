from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse

from product_extend.models import Product
from scrap.scrap_module.compiler import DataCompiler

from collections import OrderedDict

import json
import logging

logger = logging.getLogger(__name__)

# Register sites here
from scrap_module.sites.trademark import Trademark


@login_required
def trademark_site(request):
	"""
	access to the produt database is available here, making a request to save/check the data
	for storage inside the database
	"""
	
	# site data from scrap program
	trademark = Trademark().getProducts( Trademark().getCategoryLinks() )

	# access the data structure we need to save in the db
	trademark_data = DataCompiler().getPythonData( trademark )



	with transaction.atomic():
		for item in trademark_data:
			try:
				if Product.objects.filter(
					product_name=item['product_name'], 
					product_price=item['product_price'], 
					product_slug_url=item['product_slug_url'],
					product_category=item['product_category'],
					product_img=item['product_img'],
					product_website_url=item['product_website_url'],
					product_website_name=item['product_website_name']
					).exist():
					pass
				else:
					logger.debug('Inserting %r into products', item)
					data_store = Product.objects.get_or_create(**item)
					# data_model = Product()
					data_store.save()
				
			except Exception, e:
				# "Not inserted ==>", into database
				pass
	return HttpResponse(
		'<h1>Products saved!</h1><br\>'
		'<br\><h2>Inserted into db</h2><br\>' 
		'<h4>Below is the raw data scrapped from website, converted from python into json format</h4> <br\>%r ' % json.dumps( OrderedDict( trademark ) ) 
		) 
	

	


    

   