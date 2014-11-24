# -*- coding: utf-8 -*-
from connection import ScrapeBase

import urlparse
import urllib2
import json


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

  
    def filterTags( self, element_tag, product_category_link  ):
        """
        Method to filter tags with the necessary category links to access the products later
        """
        # Creating possible option to choose any string
        # if len( str( element_tag ) ) == 0:
        #     return None
        # else:
        #     return element_tag

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


    def getCategoryLinks( self, website_link, tag_link, attribute_selector, container ):
        """
        Method retrieves category links and saves them in the format: [ u'category_url', [u'productCategory_name'] ]
        """
        
        # This is the container we are searching against and pull the information
        extract_links = [ x for x in ScrapeBase().getSoup( website_link ).find_all( tag_link ) if x.get( attribute_selector ) == [u'' + container] ] 
        
        # Create search matrix to continue and search through the element and return possible numbers that could match
        container_index = [0,1,2,3,4,5,6,7,8,9]
        try:
            for i in container_index:
                if extract_links in container_index:
                    return self.filterTags(container_index[i])
        except Exception, e:
            return e, "Not in Range!"


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
                products = ScrapeBase().getSoup( link[0] ).find_all( )
            elif products:
                products = []
                
            # To add the product information that will be
            # dictionary item_name: ProductInformation items inside a new list
            productsList = []

            # Empty dictionary to store the actual product data by category
            product = {}


            # Iterate over the current pages per category, extracting all the information from all the pages
            # if not need after evaluation of the page, then comment out or we should fix a structure to allow the script to 
            # be smart enough to know when use this case or not
            current_page = link[0]
            print "current page: " + current_page
            breakout = False
            
            while ( not breakout ):
           
                for item in products:
                    
                    product['name'] = 

                    product['product_slug_url'] = 

                    product['product_img'] = 

                    try:
                        product['product_price'] = 
                    except AttributeError: 
                        return 0

                    product['product_website_url'] = self.SiteRegisterUrl('')
                    product['product_website_name'] = self.SiteRegisterName('')
                    product['product_category'] = link[1][0]

                    # append the product dictionary in the new list
                    productsList.append(product)

                # Gets the next page but if not need after evaluation of the page, then comment out or we should fix a structure to allow the script to 
                # be smart enough to know when use this case or not
                next_page = self.getNextPage( current_page )
                current_page = next_page
                print next_page + "Getting next page"
                if ( next_page != "None" ):
                    # reassigning the products variable to find products for the given page
                    products = ScrapeBase().getSoup( next_page ).find_all("a", class_="product-link")
                else:
                    # This gets out of the while loop
                    breakout = True

            
            #products is a list of product dictionaries
            #remember how link is [u'site', [u'productCategory']]
            #we'll use productCategory to the products.
            #so dict will be {'jackets' : listOfJacketProdcuts, ... }
            product_dict[ link[1][0] ] = productsList
        return product_dict

    def getNextPage(self, link_to):
        """
        Method for sites having items in more than one page
        """
        try:
            # Thsi finds the pagination link on the product page allowing to span the site.
            next_page = self.SiteRegisterUrl('') + ScrapeBase().getSoup( link_to ).find('a', class_="").get('href').strip()
            print "Next page " + next_page
            
            return next_page
        except Exception, e:    
            print "\nNo new page"
            
            return e, "None"

            
 # For Testing Purposes
if __name__=="__main__":

    categoriesClass = SiteMethods(div).filterTags('','')


    print categoriesClass
   

   