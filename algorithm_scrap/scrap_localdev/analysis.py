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

	def areSiblings(self, e1, e2):
		if e1 is None or e2 is None: return False
		if e1.parent is None or e2.parent is None: return False
		return e2.parent == e1.parent


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


	def getContainer(self): # now we're going to
		imgs = self.soup.find_all('img')

		numOfImgs = len(imgs)
		
		possibleElements = None

		while len(imgs) > 0 and possibleElements is None:
			
			for i in range(len(imgs)):
				imgs[i] = imgs[i].parent
			
			imgs = [img for img in imgs if img is not None]
			

			for i in range(len(imgs)):
				
				siblings = []
				for n in range(len(imgs)):
					if i == n: continue
					
					if (self.areSiblings(imgs[i], imgs[n])):
						siblings.append(n)

#				print "number of sibs", len(siblings)
#				if len(siblings) > 0:
#					print "a", imgs[siblings[0]].name, "with attrs:", imgs[siblings[0]].attrs
#				print
				if (len(siblings) / float(numOfImgs) > .3):
					possibleElements = siblings
					break
					
		if possibleElements is None or len(possibleElements) == 0: return None
					
		OverOne = 0
		for sib in possibleElements:
			if len(list(imgs[sib].find_all('img'))) > 1: OverOne = OverOne + 1

		if OverOne / float(len(possibleElements)) < .3:
			return imgs[possibleElements[0]].attrs
		
		while True:
			allChildren = []
			for el in possibleElements:
				allChildren.extend([x for x in imgs[el].children if x.name is not None])

			OverOne = 0
			for child in allChildren:
				if len(list(child.find_all('img'))) > 1: OverOne = OverOne + 1
			if OverOne / float(len(possibleElements)) < .3:
				return allChildren[0].attrs




	def getSoup(self):
		return self.soup


	def findElement(self, e, dict, path):
#		print path
		for element in e.children:
			if element.name is None: continue

			broke = False
			for key in dict.keys():
				broke = True
				if key == "name":
					if element.name != dict["name"]:
						break
					else:
						broke = False
						continue
				if not key in e.attrs: break
				if e.attrs[key] != dict[key]: break
				broke = False

			if not broke:
				return path + [element.name]
			recusion = self.findElement(element, dict, path + [element.name])
			if recusion is not None:
				return recusion

	def getImg(self, container):
		cont = None
		
		if "class" in container:
			c = container["class"]
			cont = filter(lambda x: x['class']==c, self.soup.find_all(**container))[0]
		elif "class_" in container:
			c = container["class_"]
			cont = filter(lambda x: x['class']==c, self.soup.find_all(**container))[0]
		else:
			cont = self.soup.find(**container)
		return self.findElement(cont, {"name":"img"}, [])



# For Testing Purposes
if __name__=="__main__":
	SiteUrl = raw_input("what's website (just www.something.com): ")
	ProductsPage = raw_input("where are the products (like www.something.com/store): ")
	name = raw_input("what's the name of the site")

	if ProductsPage.endswith('/'):
		ProductsPage = ProductsPage[:len(ProductsPage)-1]

	analysis = Analysis(ProductsPage)
	analysis.loadSoup()
	print ProductsPage
	container = analysis.getContainer()
	print container


	method = """
def swordsSmith():
	site = SiteMethods()


	siteUrl = '""" + SiteUrl + """'

	site.setUrl('"""  + ProductsPage + """')
	site.setBaseUrl(siteUrl)
	site.setName('""" + name + """')

	site.setCategoryPath([ {"class_":"main-content"}, {"class_":"grid-nav"}, 'li[all]', 'a' ])
	links = site.getCategories()

	for i in range(len(links)):
		if (links[i][1].startswith('/')):
			links[i][1] = siteUrl + links[i][1]

	site.setProductContainer(""" + str(container) + """)
	site.setImage( ['a', 'img'] )
	site.setProductLink( ['a'] )
	site.setProductName( ['a', {"class_":"product-name"}, '.contents[0]' ] )
	site.setPricePath([ {"class_":"product-price"}, '.contents' ])


	site.setProductPageSizePath([ {"id":"js-product-detail-size-list"}, 'ul', 'li[all]', '.contents' ])
		site.setProductPageDescriptionPath([ {"class_":"product-detail-description"}, 'span', 'p', '.contents' ])
"""

	print analysis.getImg(container)

