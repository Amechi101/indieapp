from django.db import transaction
from django.http import HttpResponse

from _backend_api.models import Product

from scrap_module.utils.compiler import DataCompiler
from scrap_module.sites.trademark import Trademark

import logging

logger = logging.getLogger(__name__)


def _trademark(request):
	"""
	access to the produt database is available here, making a request to save/check the data
	for storage inside the database
	"""
	
	# site data from scrap program
	trademark = Trademark().getProducts( Trademark().getCategoryLinks() )

	# access the data structure we need to save in the db
	trademark_data = DataCompiler().getPythonData( trademark )

	# Show the name of items inserted in DB
	items_inserted = []

	# counter for each item scrapped in total
	items_counter = 0


	with transaction.atomic():
		for item in trademark_data:
			try:
				data_store = Product.objects.get_or_create( product_slug_url=item['product_slug_url'], website_id=1, defaults=item )

				if data_store:
					# Logging for Django purposes
					logger.debug('Inserting %r into products', item )
			
					items_inserted.append( item['product_name'] )

					items_counter += 1

					data_count = Product.objects.filter( website_id=1 ).count()

					data_store.save()

				else:
					data_store.update(**item)
				
			except Exception:
				# "Not inserted ==>", into database
				logger.exception('Something went wrong inserting a new entry %r', item )

	return HttpResponse('<h1>Products saved!</h1><br\>'
						'<h2> %r Total Products Scrapped</h2><br\>'
						'<h4> %r  Products Currently in db</h4><br\>'
						'<div><ul> <li>%s</li> </ul></div>'% (items_counter, data_count, items_inserted )
						) 
	

	


    

   