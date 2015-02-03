#!/usr/bin/env python
class DataCompiler( object ):
	"""
	Class getting all site data, accessing the data, then flattening the data into a list
	"""

	def getPythonData( self, python_data ):
		"""
		Generator function mapping the data into the 'Product' model in django for storage into the database
		"""
		for key in python_data:
  			list_categories = python_data[key]
  			
  			for category in list_categories:
  				yield category 





