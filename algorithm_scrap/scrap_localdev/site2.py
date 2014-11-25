# -*- coding: utf-8 -*-
from connection import ScrapeBase

import urlparse
import urllib2
import json

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
	
	def setUrl(self, url):
		self.url = url
	
	
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
	
	
	
	def setProductPageSizePath(self, path):
		self.productPageSizePath = path
	
	def setProductPageColorPath(self, path):
		self.productPageColorPath = path
	
	def setProductPageDescriptionPath(self, path):
		self.productPageDescriptionPath = path
	
	#	def setProductPageContainer(self, container):
	#		self.ProductPageContainer = container
	
	
	def find(self, element, steps):
		try:
			for i, step in enumerate(steps):
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
			return None
		
		return element
	
	def getCategories(self):
		print "getting soup"
		soup = ScrapeBase().getSoup(self.url)
		print "finished"
		return [x['href'] for x in self.find(soup.html, self.categoryPath)]
	
	
	
	def go(self):
		print "getting soup"
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
			
			product = { }
			
			if self.productLinkPath:
				product['url'] = self.find(div, self.productLinkPath)['href']
			if self.imagePath:
				product['img'] = self.find(div, self.imagePath)['src']
			if self.namePath:
				product['name'] = self.find(div, self.namePath).contents
			if self.pricePath:
				product['price'] = self.find(div, self.pricePath).contents
			
			
			results = self.checkProductPage(product['url'])
			
			product.update(results)
			
			products.append(product)
		
		
		return products
	
	
	def checkProductPage(self, url):
		
		product = { }
		
		soup = ScrapeBase().getSoup(url)
		
		if self.productPageSizePath:
			product['sizes'] = self.find(soup.html, self.productPageSizePath)
		if self.productPageColorPath:
			product['colors'] = self.find(soup.html, self.productPageColorPath)
		if self.productPageDescriptionPath:
			product['description_long'] = self.find(soup.html, self.productPageDescriptionPath)
		
		return product
	
	
	
	
	
	def filterTags( self, element_tag, product_category_link  ):
		"""
			Method to filter tags with the necessary category links to access the products later
			"""
		# Creating possible option to choose any string
		# if len( str( element_tag ) ) == 0:
		#	 return None
		# else:
		#	 return element_tag
		
		# Finding tag with descendants where the category link would live
		find_tag = [ x for x in self.html_tag.descendants if x.name == element_tag ]
		
		#Setting the apporiate index to find the links throughout the site,
		#this index wiil scan the site against this array,looking for the proper HTML tag to filter
		# It is set with numbers from 0 - 10 as from experience anything outside the range would indicate
		# that we must change the tag in filter tags list filter
		tag_index = [0,1,2,3,4,5,6,7,8,9,10]
		try:
			for i in tag_index:
				if tag_index[i]:
					tag = find_tag[i]
				else:
					return []
		except Exception, e:
			return e, "Not in Range!"
		
		
		# Returning the links and the contents within the links in a new list
		return [ [x.get('href'), x.contents ] for x in tag.find_all('a') if x.get('href').strip().startswith( product_category_link ) ]


def test():
	return pilgrimsurfsupply()


def pilgrimsurfsupply():
	site = SiteMethods()
	
	
	site.setUrl('http://pilgrimsurfsupply.com/store/')
	site.setProductContainer(class_=['product_cell'])
	site.setCategoryPath([ {"id":"category-tree"}, 'li', 'ul', 'li[all]', 'a' ])
	site.setImage( [ {"class_":"product_cell_graphic"}, 'a', 'img'] )
	site.setProductLink( [{"class_":"product_cell_graphic"}, 'a'] )
	site.setProductName( [{"class_":"product_cell_label"}, 'a'] )
	site.setPricePath([ {"class_":"product_cell_price"} ])
	
	
	site.setProductPageSizePath([ {"id":"SelectSize"}, 'option[all]', '.contents' ])
	site.setProductPageColorPath([ {"id":"SelectColor"}, 'option[all]', '.contents' ])
	site.setProductPageDescriptionPath([ {"id":"Product_description_long"}, '.contents' ])
	
	return site.getCategories()



# For Testing Purposes
if __name__=="__main__":
	print test()



