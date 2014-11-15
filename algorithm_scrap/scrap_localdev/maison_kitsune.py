# -*- coding: utf-8 -*-
from connection import ScrapeBase

import urllib2
import json

class MaisonKitsune( object ):
    
    def getCategoryLinks( self ):
        """
        This method retrieves category links from the homepage and saves them in this format [ u'category_url', [u'productCategory_name'] ]
        """
        def filterTags( html_tag ):

            #Finding the tag that wraps around the content we need within descendants
            find_tag = [ x for x in html_tag.descendants if x.name == 'ul' ] 
            
            #Getting the first tag within the  children
            tag_index = find_tag[0]
           
            # Returning the links and the contents within the links in a new list
            return [ [x.get('href'), x.string  ] for x in tag_index.find_all('a') if x.get('href').strip().startswith("http://shop.kitsune.fr/maison-kitsune/man/") ]
       
        # This is the container we are searching against
        extract_links = [ x for x in ScrapeBase().getSoup("http://shop.kitsune.fr/?___store=kitsune_fr_usa&___from_store=kitsune_fr_usa").find_all('div') if x.get('class') == [u'nav-container'] ] 

        # The call to the inner function
        return filterTags(extract_links[0])

    def getProducts( self, links ):
        """
        1. This method filters through 'x' amount of pages of the nasty gal website using the link's scraped from the method getCategories()
        2. This method filters through 'x' pages using 1. and retrieves product information from 'x' amount of products on the current page
        """

        # a new dictionary
        product_dict = {} 
    
        for link in links:
            # link is [ u'site', [u'productCategory'] ], but site is unicode object. Convert it to a string
            link[0] = str(link[0]) #This is the site URL
            link[1] = str(link[1])  #This is the productCategory

        
            # A nice control statement to direct the flow a little better
            # to allow for more custom loops to pick different items and etc..
            
            # Main Product information
            products = None
            supplement_information = None
            if link[0]:
                products = ScrapeBase().getSoup( link[0]).find_all("li", class_="product-fader-wrapper")
                # supplement_information = ScrapeBase().getSoup( link[0]).find_all("a", class_="product-link")
                print link[0]
            elif products:
                products = []
            

            # To add the product information that will be
            # dictionary item_name: ProductInformation items inside a new list
            productsList = []

            # Empty dictionary to store the actual product data by category
            product = {}
            
           
               
            for item in products:
            
                product['name'] = item.find('a', class_="product-image-link").get('title')

                # product['product_url'] = item.get('href').strip()

                # product['img'] = item.find('img').get('src')[2:]

                # try:
                #     product['price'] = item.find("span", class_="current-price").text.strip()
                # except ValueError: 
                #     print ("Non-numeric data! Please Change.")
            
                
                # #Designers are in the title of the product name
                # #but not constant enough to scrap in completion, so we must manually add
                # #the designers to each product from or figure a method to extract each name
                # # for the product being scrap
                # product['designer_name'] = ''

                # product['Category'] = link[1]


                # append the product dictionary in the new list
                productsList.append(product)
                
                

            
            # For scrapping supplementary information about the brand not in the 
            # list searching against the product
            # for supplement in supplement_information:
            #     product['website_home_url'] = "http://www.nastygal.com"
            #     product['name_of_brand'] = "Nasty Gal"


            #products is a list of product dictionaries
            #remember how link is [u'site', [u'productCategory']]
            #we'll use productCategory to the products.
            #so dict will be {'jackets' : listOfJacketProdcuts, ... }
            product_dict[ link[1] ] = productsList
        return product_dict



if __name__=="__main__":
    
    categoriesClass = MaisonKitsune().getCategoryLinks()
    categoriesProductsClass = MaisonKitsune().getProducts(categoriesClass)
    
    # out = open("output_files/mk.txt", 'w')
    # out.write(json.dumps(categoriesProductsClass))

    # print categoriesProductsClass.keys()

    # print categoriesClass
    print categoriesProductsClass
    
   