# -*- coding: utf-8 -*-
from connection import ScrapeBase

import urlparse
import urllib2
import json
from utils import *

import sys, os


class SiteMethods( ScrapeBase ):
	"""
		Global site methods to Filter against tags locating product category tags
		
		"""
	def __init__( self, *args, **kwargs ):
		super(SiteMethods, self).__init__( *args, **kwargs )
	
	
	def SiteRegisterUrl(self, site_url=''):
		"""
			register the websites url begin used
			"""
		
		if site_url != '':
			site_path =  urlparse.urlparse(site_url).path.split('/')[-1]
			
			return site_path
	
	def SiteRegisterName(self, site_name):
		"""
			register the websites name begin used
			"""
		return site_name
	
	
	def setBaseUrl(self, url):
		self.baseUrl = url
	
	def setUrl(self, url):
		self.url = url
	
	def setCategory(self, category):
		self.category = category
	
	def setProductContainer(self, **container):
		self.container = container
	
	def setImage(self, path):
		self.imagePath = path
	
	def setProductLink(self, path):
		self.productLinkPath = path
	
	def setProductName(self, path):
		self.namePath = path
	
	def setPricePath(self, path):
		self.pricePath = path
	
	def setCategoryPath(self, path):
		self.categoryPath = path
	
	def setName(self, name):
		self.name = name
	
	
	
	def setProductPageSizePath(self, path):
		self.productPageSizePath = path
	
	def setProductPageColorPath(self, path):
		self.productPageColorPath = path
	
	def setProductPageDescriptionPath(self, path):
		self.productPageDescriptionPath = path
	
	#	def setProductPageContainer(self, container):
	#		self.ProductPageContainer = container
	
	
	def find(self, element, steps):
		for i, step in enumerate(steps):
			try:
				if type(step) is dict:
					element = element.find(**step)
				
				elif type(step) is str:
					index = step.find('[')
					if step.startswith('.'):
						element = eval("element" + step)
					elif (index == -1): #not found
						element = element.find(step)
					else:
						pos = step[index+1:step.find(']')]
						if (pos == 'all'):
							return [self.find(x, steps[i+1:]) for x in element.find_all( step[:index] )]
						pos = int(pos)
						element = element.find_all(step)[pos]
						
			except Exception, e:
				
				#print exception type, file name, and line number
				exc_type, exc_obj, exc_tb = sys.exc_info()
				fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
				print(exc_type, fname, exc_tb.tb_lineno)
				print "on step", step, "in", steps
				print "element == None:", element == None
				if element is not None:
					print "element was a", element.name, "with", element.attrs
				print
				return None
		
		return element
	
	
	def isAllCategories(self, name):
		if (type(name) is list): name = name[0]
		name = str(name).lower()
		print name
		return 'category' in name or name.startswith('all ')
	
	def getCategories(self):
		print "getting soup from " + self.url
		soup = ScrapeBase().getSoup(self.url)
		print "finished"
		return [[x.contents, x['href']] for x in self.find(soup.html, self.categoryPath) if not self.isAllCategories(x.contents)]
	
	
	
	def go(self):
		print "getting soup from " + self.url
		soup = ScrapeBase().getSoup(self.url)
		print "finished"
		
		divs = None
		
		if self.container:
			divs = soup.find_all(**self.container)  # finds all the divs that contain products
		else:
			divs = soup.find_all('div') # if the container isn't defined, just find all the divs
		
		divs = [x for x in divs if x is not None] # makes sure we don't have any Nones in our array
		
		divs = divs[0:1] # for testing, we only want one div
		
		products = [ ]

		for div in divs:
			
			product = {"product_website_url": self.url, "product_website_name": self.name }
			
			if hasattr(self, "namePath"):
				product['name'] = self.find(div, self.namePath)
			if hasattr(self, "productLinkPath"):
				product['product_slug_url'] = self.find(div, self.productLinkPath)['href']
			if hasattr(self, "imagePath"):
				try:
					product['product_img'] = self.find(div, self.imagePath)['src']
				except KeyError: # swords smith has a <img /> somewhere that doesn't have a src attribute. What's this world come to
					product['product_img'] = "http://www.designjenesis.com/web120/a6/images/unavailable.png"
			if hasattr(self, "pricePath"):
				product['product_price'] = self.find(div, self.pricePath)
			if hasattr(self, "category"):
				product['product_category'] = self.category
			
			
			results = self.checkProductPage(product['product_slug_url'])
			
			product.update(results)
			
			products.append(product)
		
		
		return products
	
	
	def checkProductPage(self, url):
		
		product = { }
		
		if (url.startswith('/')):
			url = self.baseUrl + url
		
		soup = ScrapeBase().getSoup(url)
		
		if hasattr(self, "productPageSizePath"):
			product['sizes'] = self.find(soup.html, self.productPageSizePath)
		if hasattr(self, "productPageColorPath"):
			product['colors'] = self.find(soup.html, self.productPageColorPath)
		if hasattr(self, "productPageDescriptionPath"):
			product['description_long'] = self.find(soup.html, self.productPageDescriptionPath)
		
		return product


def test():
	data = swordsSmith()
	if isHealthy(data): print "data is healthy"
	else: print "data is unhealthy"
	return data

def pilgrimsurfsupply():
	site = SiteMethods()
		
		
	siteUrl = 'http://pilgrimsurfsupply.com'
	
	site.setUrl('http://pilgrimsurfsupply.com/store/')
	site.setBaseUrl(siteUrl)
	site.setName("Pilgrim Surf Supply")

	site.setCategoryPath([ {"id":"category-tree"}, 'li', 'ul', 'li[all]', 'a' ])
	links = site.getCategories()

	for i in range(len(links)):
		if (links[i][1].startswith('/')):
			links[i][1] = siteUrl + links[i][1]

	site.setProductContainer(class_=["product_cell"])
	site.setImage( [ {"class_":"product_cell_graphic"}, 'a', 'img'] )
	site.setProductLink( [{"class_":"product_cell_graphic"}, 'a'] )
	site.setProductName( [{"class_":"product_cell_label"}, 'a', '.contents'] )
	site.setPricePath([ {"class_":"product_cell_price"}, '.contents' ])
	
	
	site.setProductPageSizePath([ {"id":"SelectSize"}, 'option[all]', '.contents' ])
	site.setProductPageColorPath([ {"id":"SelectColor"}, 'option[all]', '.contents' ])
	site.setProductPageDescriptionPath([ {"id":"Product_description_long"}, '.contents' ])
	
	
	products = []
	for category, link in links:
		if (type(category) is list): category = category[0]
		site.setCategory(category)
		site.setUrl(link)
		products.extend(site.go())
	return products


def swordsSmith():
	site = SiteMethods()
	
	
	siteUrl = 'http://swords-smith.com'
	
	site.setUrl('http://swords-smith.com/collections/womens-clothing-and-accessories')
	site.setBaseUrl(siteUrl)
	site.setName("Swords Smith")
	
	site.setCategoryPath([ {"class_":"main-content"}, {"class_":"grid-nav"}, 'li[all]', 'a' ])
	links = site.getCategories()
	
	for i in range(len(links)):
		if (links[i][1].startswith('/')):
			links[i][1] = siteUrl + links[i][1]
	
	site.setProductContainer(class_="product")
	site.setImage( ['a', 'img'] )
	site.setProductLink( ['a'] )
	site.setProductName( ['a', {"class_":"product-name"}, '.contents[0]' ] )
	site.setPricePath([ {"class_":"product-price"}, '.contents' ])
	
	
	site.setProductPageSizePath([ {"id":"js-product-detail-size-list"}, 'ul', 'li[all]', '.contents' ])
	site.setProductPageDescriptionPath([ {"class_":"product-detail-description"}, 'span', 'p', '.contents' ])
	
	
	products = []
	for category, link in links:
		if (type(category) is list): category = category[0]
		site.setCategory(category)
		site.setUrl(link)
		products.extend(site.go())
	return products




# For Testing Purposes
if __name__=="__main__":
	print test()



