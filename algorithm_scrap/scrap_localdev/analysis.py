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



	def getSiblings(self, element):
		return [x for x in element.parent.children if x.name is not None]


	def isSimilar(self, e1, e2):
		if (e1 == e2): return True

		children1 = [x for x in e1.children if x.name is not None]
		children2 = [x for x in e2.children if x.name is not None]

		if len(children1) != len(children2):
			print len(children1), " is not ", len(children2)
			print [x.name for x in children1], " vrs ", [x.name for x in children2]
			return False

		length = len(children1)

		if length == 0:
			print e1.name, "vrs", e2.name
			return e1.name == e2.name

		return all([self.isSimilar(children1[i], children2[i]) for i in range(length)])

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

	def getTags2(self): # now we're going to
		divs = filter(self.isntWorthLess, self.soup.find_all('div'))

		possiblities = []

		for div in divs:
			siblings = list(self.getSiblings(div))
			print len(siblings)



	def getSoup(self):
		return self.soup




def test():
	analysis = Analysis("http://pilgrimsurfsupply.com/store/")
	analysis.loadSoup()
	soup = analysis.getSoup()
	p = soup.find(class_='product_cell')
	sibs = list(analysis.getSiblings(p))
	print [analysis.isSimilar(sibs[0], sibs[i]) for i in range(3)]


# For Testing Purposes
if __name__=="__main__":
	analysis = Analysis("http://pilgrimsurfsupply.com/store/")
	analysis.loadSoup()
	print analysis.getTags2()



