# -*- coding: utf-8 -*-
from connection import ScrapeBase

import urlparse
import urllib2
import json

import sys, os


class Analysis( ScrapeBase ):
	"""
	Runs analysis on a website to try to find appropioate tags and code
		
	"""

	def __init__(self, mainUrl):
		self.url = mainUrl

	def loadSoup(self):
		print "getting soup from " + self.url
		self.soup = ScrapeBase().getSoup(self.url)
		print "done"


	def getSigniture(self, container):
		if hasattr(container, "children"):
			children = [x for x in container.children if x.name is not None]
			if len(children) > 0:
				return container.name + ''.join([self.getSigniture(x) for x in children])
			else:
				return container.name
		elif container.name is not None:
			return "ff"#container['id']


	def isntWorthLess(self, container):
		try:
			return len([x for x in container.children if x.name is not None]) > 0
		except:
			return False


def getTags(self): # this method didn't work out, turns out the most common div isn't the product divs
		if not hasattr(self, "soup"):
			print "Please loadSoup() before calling getTags"
			return
		containers = filter(self.isntWorthLess, self.soup.find_all('div'))

		childrenSignitures = [self.getSigniture(x) for x in containers]
		childrenSignitures = filter(lambda x: x, childrenSignitures) # filters out None


		sigs = set(childrenSignitures) # eliminate mulitple occurences

		mostCommon = max(sigs, key=childrenSignitures.count)

		return mostCommon





	def getSoup(self):
		return self.soup








# For Testing Purposes
if __name__=="__main__":
	analysis = Analysis("http://pilgrimsurfsupply.com/store/")
	analysis.loadSoup()
	print analysis.getTags()



