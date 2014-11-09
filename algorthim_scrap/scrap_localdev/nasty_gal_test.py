# -*- coding: utf-8 -*-
from base import ScrapeBase

# import urllib2
# import json

class NastyGal( ScrapeBase ):
    
    def getCategoryLinks( self ):
        """
        This method retrieves category links from the homepage and saves them in this format [ u'category_url', [u'productCategory_name'] ]
        """
        def filterTags( html_tag ):

            uls = [ x for x in html_tag.descendants if x.name == 'ul' ] #Finding ul within descendants
            ul = uls[0] #Getting the first ul within the divs children
            
            # Returning the links and the contents within the links in a new list
            return [ [x.get('href'), x.contents ] for x in ul.find_all('a') if x.get('href').strip().startswith("http://www.nastygal.com/clothes-") ]
       
        # This is the container we are searching against
        divs = [ x for x in ScrapeBase().getSoup("http://www.nastygal.com/clothes").find_all('div') if x.get('class') == [u'container'] ] 

        # The call to the inner function
        return filterTags(divs[0])

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
            link[1][0] = str(link[1][0])  #This is the productCategory

        
            # A nice control statement to direct the flow a little better
            # to allow for more custom loops to pick different items and etc..
            products = None
            if link[0]:
                products = ScrapeBase().getSoup( link[0]).find_all("a", class_="product-link")
                print link[0]
            elif products:
                products = []
            

            # To add the product information that will be
            # dictionary item_name: ProductInformation items inside a new list
            productsList = []
            
            current_page = link[0]
            print "current page: " + current_page
            breakout = False

            while (not breakout):
               
                for item in products:
                
                    product = {}
                    
                    product['name'] = item.find('div', class_="product-name").text.strip()

                    product['product_url'] = item.get('href').strip()

                    product['img'] = item.find('img').get('src')[2:]

                    try:
                        product['price'] = item.find("span", class_="current-price").text.strip()
                    except ValueError: 
                        print ("Non-numeric data! Please Change.")
                
                    
                    #Designers are in the title of the product name
                    #but not constant enough to scrap in completion, so we must manually add
                    #the designers to each product from or figure a method to extract each name
                    # for the product being scrap
                    product['designer_name'] = ''

                    # Must figure methods to get this information automatically instead of manually writing these two values
                    # for every site we scrap
                    product['website_home_url'] = "http://www.nastygal.com"
                    product['name_of_brand'] = "Nasty Gal"
                    product['Category'] = link[1][0]

                    
                    # append the product dictionary in the new list
                    productsList.append(product)
                    
            
    
                print "Getting next page"
                next_page = self.getNextPage(current_page)
                current_page = next_page
                print next_page
                if (next_page != "None"):
                    products = ScrapeBase().getSoup(next_page).find_all("a", class_="product-link")
                else:
                    breakout = True

            #products is a list of product dictionaries
            #remember how link is [u'site', [u'productCategory']]
            #we'll use productCategory to the products.
            #so dict will be {'jackets' : listOfJacketProdcuts, ... }
            product_dict[ link[1][0] ] = productsList
        return product_dict


    def getNextPage(self, link_to):
        try:
            next_page = "http://www.nastygal.com" + ScrapeBase().getSoup(link_to).find('a', class_="js-ajax next").get('href').strip()
            print "Next page " + next_page
            return next_page
        except:    
            print "\n\nNo new page"
            return "None"




    
   