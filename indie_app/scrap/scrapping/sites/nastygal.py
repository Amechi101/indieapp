from bs4 import BeautifulSoup
import urllib2
import requests
import sqlite3

class nastygal():
	def keyword_Search_Shoptiques(self, keyword):
		""" 
		get all products for the given keyword
		"""
		#self.url is now a global instance variable

		clothes = urllib2.urlopen("http://nastygal.com/clothes").read()
		file = open("out.txt", 'w+')
		file.write(clothes)
		file.close()
		file = open("out.txt", 'r')
		text = file.read()
		print "successfully opened it"
		#figure out how to actually get a search page for the keywords -- will be altering the URL for each keyword search
		#self.url = requests.get("http://nastygal.com/clothes/?seg=5")
		#data = self.url.text
		soup = BeautifulSoup(text)

		self.product_counter = -1

		self.products = soup.find_all("a", class_="product-link")

		self.items = len(self.products)

		#create counter for the next_product specifically for shoptiques
		#self.product_counter = -1

		#create the products which is the array of products
		#self.products = soup.find("div", id="productHolder")

	#<div class="product with-swatches listproduct" id="p-34072">


	def get_Next_Product_Shoptiques(self):
		"""
		gets the next product list and returns it so the comparison can take place in the keyword_search method
		""" 
		print "Total = " + str(len(self.products))
		self.product_counter = self.product_counter + 1
		print "Counter = " + str(self.product_counter)
		if (self.product_counter < len(self.products)):
			self.product_title = self.products[self.product_counter].find("div", class_="product-name").text.strip()
			return self.product_title
		else: 
			return 0


		#get id = productHolder and then get the child and the siblings of the child - will iterate through all the products
		#every odd is a valid product
		#self.product_counter = self.product_counter + 2
		#print self.product_counter
		#if (self.product_counter < len(self.products.contents)):
		#	if self.product_counter % 2 != 0:
				#getting divs with product holder id, getting paragraph within those, stripping the text 
		#		product_title = self.products.contents[self.product_counter].find("p").text.strip()
				
		#		print self.product_counter
		#		return product_title
		#else:
		# 	return 0 

	#iterate products.contents[0] to get the div

	#what to do when no more products?


	def scrape_item_Shoptiques(self):
		"""
		Go into the current item product page for the item and scrape it
		"""

		self.url = requests.get("http://nastygal.com/clothes/?seg=5")
		data = self.url.text
		soup = BeautifulSoup(data)

		#get the items URL
		product_url = self.products[self.product_counter].get('href')
		#print "Product URL: " + product_url

		
		#create new soup item for the new page
		full_product_url = requests.get(product_url)
		product_data = full_product_url.text
		p_soup = BeautifulSoup(product_data)

		
		#start extracting things from product page

		return (self.product_title, self.getPrice(p_soup), self.getBoutique(p_soup), self.getColors(p_soup), self.getDescription(p_soup), self.getDesigner(p_soup), self.getImages(p_soup)  )

 	

 		
 		#	get description
 		

 		#	get brand/designer
 		

 		# get images
 		



 		#=========== methods ==============

 	def getPrice(self, soup):
 		price = soup.find("span", class_ = "current-price").text
		return str(price)


	def getBoutique(self, soup):
		#boutique = soup.find("span", clothesass_="boutique-links").text.strip()
 		return "None"



 	def getColors(self, soup):
		return "None"		


	def getDescription(self, soup):
		# get outer div
 		description_div = soup.find("div", class_ = "product-description")
 		
 		return str(description_div.text.strip())


 	def getDesigner(self, soup):
 		return "None"

 	def getImages(self, soup):
 		#get the image gallery div
 		images_list = []
 		images = soup.find_all("img")
 		for image in images:
 			if image.has_key("data-zoom"):
 				images_list.append(str(image.get("src")))
 				#print image.get("src")
 		return images_list
