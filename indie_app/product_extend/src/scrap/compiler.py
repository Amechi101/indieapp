# -*- coding: utf-8 -*-
#!/usr/bin/env python

from nastygal import NastyGal
from trademark import TrademarkScrape
from hawthorn import Hawthorn 

import json


class DataManipulate( object ):
	"""
	Class to get all the site data and save it in a python object
	"""

	def runSiteScript(self):

		# New dictionary for site web scrapping
		scrapped_sites = {}

		# Inputting the sites inside the script
		scrapped_sites['Trademark'] = TrademarkScrape().getProducts( TrademarkScrape().getCategoryLinks() )
		# scrapped_sites['NastyGal'] = NastyGal().getProducts( NastyGal().getCategoryLinks() )
		# scrapped_sites['Hawthorn'] = Hawthorn().getProducts( Hawthorn().getCategoryLinks() )

		return scrapped_sites
		
	def getJsonData( self, json_data ):
		
		# Retrieve the data  in JSON format
		fetch = json.dumps(json_data, ensure_ascii=False).encode('utf8')

		# Load the data and ready it for the data base storage convert it to Python Object
		result = json.loads(fetch)

		return result


		
if __name__=="__main__":

	master_data = DataManipulate().runSiteScript()
	
	acquire_json = DataManipulate().getJsonData( master_data )

	print acquire_json['Trademark']

	# out = open("output_files/final.json", 'w')
	# out.write(acquire_json )


