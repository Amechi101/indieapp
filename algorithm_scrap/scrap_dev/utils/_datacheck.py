
def isHealthy(data):
	"""
	checks to see if the results have all the required data
	"""
	healthy = True
	required = ['name', 'product_slug_url', 'product_img', 'product_price', 'product_website_url', 'product_website_name', 'product_category']
	
	for i, d in enumerate(data):
		for key in required:
			if key not in d or d[key] is None:
				print "data[" + str(i) + "] is missing key", key
				healthy = False
	return healthy