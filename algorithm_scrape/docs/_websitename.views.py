from django.db import transaction
from django.http import HttpResponse

from product_extend.models import Product

# This is what flattens the dictionary structure to a list and enables storage into the django db 
from scrap_module.utils.compiler import DataCompiler

# enter website name from site registered in scrap/scrap_module/sites and import the class name specified
from scrap_module.sites.websitename import WebsiteClassName

import logging

logger = logging.getLogger(__name__)


def _trademark(request):
	"""
	access to the produt database is available here, making a request to save/check the data
	for storage inside the database
	"""
	
	# site data from scrap program
	websitename = WebsiteClassName().getProducts( WebsiteClassName().getCategoryLinks() )

	# access the data structure we need to save in the db
	websitename_data = DataCompiler().getPythonData( websitename )

	# Show the name of items inserted in DB
	items_inserted = []

	# counter for each item scrapped in total
	items_counter = 0


	with transaction.atomic():
		for item in websitename_data:
			try:
				# creates the data objects and places them in the apporiate tables/rows. The website id will be assigned in Step 1.
				# See the Readme.md in algorithm_scrape in github repo this id will assign the products to the correct registered website.
				# To see website id all see the docs in the repo 
				data_store = Product.objects.get_or_create( product_slug_url=item['product_slug_url'], website_id=int, defaults=item )

				if data_store:
					# Logging for Django purposes
					logger.debug('Inserting %r into products', item )
			
					items_inserted.append( item['product_name'] )

					items_counter += 1

					# Gives a count of how many items are in the database
					data_count = Product.objects.filter( website_id=int ).count()

					# saves the instance of all the products inside the database
					data_store.save()

				else:
					# updates any new items of fields inside the database
					data_store.update(**item)
				
			except Exception:
				# "Not inserted ==>", into database
				logger.exception('Something went wrong inserting a new entry %r', item )

	return HttpResponse('<h1>Products saved!</h1><br\>'
						'<h2> %r Total Products Scrapped</h2><br\>'
						'<h4> %r  Products Currently in db</h4><br\>'
						'<div><ul> <li>%s</li> </ul></div>' % (items_counter, data_count, items_inserted )
						) 
	
