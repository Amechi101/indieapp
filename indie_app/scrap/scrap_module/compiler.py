#!/usr/bin/env python
class DataCompiler( object ):
	"""
	Class to get all the site data and access that data reading it for storage
	into the database
	"""

	def getPythonData( self, python_data ):

		for key in python_data:
  			list_categories = python_data[key]
  			
  			for category in list_categories:
  				yield category 





