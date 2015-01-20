#!/usr/bin/env python

from trademark import Trademark

trademark = Trademark().getProducts( Trademark().getCategoryLinks() )

class DataManipulate( object ):
	"""
	Class to get all the site data and save it in a python object
	"""

	def getPythonData( self, python_data,  **kwargs):
		for kv in python_data:
  			print "Processing ", kv
  			lst = python_data[kv]
  			
  			for entry in lst:
  				yield entry # this goes into db under category kv




		


	# def getFromDict(self, data, mapList):
	# 	return reduce(lambda d, k: d[k], mapList, self.getData( data ))

	# def saveData( self, acquire_json, **kwargs ):

	# 	for kwargs in acquire_json:
	# 		return self.getFromDict( acquire_json, [kwargs] )


		
if __name__=="__main__":
	
	acquire_python = DataManipulate().getPythonData( trademark )

	for item in acquire_python:
	    print item['name']

	# out = open("output_files/final.json", 'w')
	# out.write( acquire_python )

	# print acquire_python


