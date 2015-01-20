#!/usr/bin/env python
from bs4 import BeautifulSoup
from selenium import webdriver

import requests
import urllib2


class ScrapeBase( object ):
	"""
	Base class representing common and abstract methods in use throughout the scrapping program
	"""

	def getHttp(self, site_url):
		"""
		Method to get HTTP Access to the websites
		"""

		# You can just ignore the headers and req stuff don't exist, but for some reason it won't work without them
        # http://stackoverflow.com/questions/13303449/urllib2-httperror-http-error-403-forbidden
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		    'Accept-Encoding': 'none',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'Connection': 'keep-alive'}
		
		req = urllib2.Request(url=site_url, headers=headers)
		
		try:
			connection = urllib2.urlopen(req) 
			return connection.read()
		except urllib2.HTTPError:
			connection = "None"
		
	def getSoup(self, site_target):
		"""
		Get website any website urls, which will be the initializer for all of the website sub classes
		"""
		soup = BeautifulSoup( self.getHttp( site_target ) )
		return soup

	def getSoupWithJSRendered(self, site_target):
		browser = webdriver.PhantomJS()
		browser.get(site_target)
		html_source = browser.page_source
		browser.quit()

		return BeautifulSoup(html_source)


		
		

