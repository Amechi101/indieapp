# -*- coding: utf-8 -*-
from scrap.scrap_module.connection import ScrapeBase

import urllib2
import json
import re


class Trademark( ScrapeBase ):
 
    def getCategoryLinks(self):  

        def filterTags(html_tag):
            uls = [x for x in html_tag.children if x.name == 'ul'] # iterate through the children of div, and add them to uls if its a <ul ...
            ul = uls[0] #There should only be one
            
            lis = [x for x in ul.children if x.name == 'li'][:2] # first two li elements of the ul element have the "women" and "men" category
            womensLi = lis[0] #The first li is of the women category. TODO add mens
            
            # return [[link, name], [link, name]....] by finding all links: find_all('a'), only if the link goes to a trademark site.
            return [[x.get('href'), x.contents[0]] for x in womensLi.find_all('a') if x.get('href').startswith("http://www.trade-mark.com/womens/")][1:]
            

        divs = [ x for x in ScrapeBase().getSoup("http://www.trade-mark.com").find_all('div') if x.get('class') == [u'nav'] ] # finds all <div class="nav">

        return filterTags(divs[0]) #There should only be one <div class="nav"> at trade-mark.com, so we'll pass this tag over to getLinks

    def getProducts(self, links):
        
        # Storing the categories and product information
        product_dict = {}
        
        for site_link, productCategory in links:
            site_link = site_link.encode('ascii') # site is unicode object. Convert it to a string

            if site_link.strip().endswith('/womens/womens-fall.html'): 
                continue

            #This is the tricky part. Simply getting the html from the site won't work.
            # The site has this in it: <div class="listing-products listing-products-alt clearfix"> </div>
            #But later, javascript runs and fills it in. Each site has an 'cat_id', and the javascript passes this id to www.trade-mark.com/solr,
            #which returns json

            html = urllib2.urlopen(site_link).read() # read the html from this url
            
            cat_id = re.search(r"var cat_id = '(\d+)';", html).group(1)

            #this call gets the responce from www.trade-mark.com/solr, using the id we have acquired
            rsp =  urllib2.urlopen("http://www.trade-mark.com/solr/"
                "?q_is_in_stock=true&q_category_ids={0}&rows=10000"
                "&fl=name,url,price,final_price,sale_price,product_id,"
                "image_varchar,alt_image_varchar,color_gpd,parent_id_int"
                "&sort=cat_{0}_co+asc".format(cat_id))



            #load this json to a python dictionary
            httpDict = json.load(rsp)

            #Array for the product objects to be stored, i.e name, image etc..
            products = []   

            #The following for loop copies the data from httpDict into product dictionary
            for doc in httpDict['response']['docs']:
                product = {}
                
                if 'final_price' not in doc:
                    # no final prices means we discard *all results*
                    return []

                product['product_name'] = doc['name']

                product['product_slug_url'] = doc['url']

                product['product_image'] = doc['image_varchar'].pop()
                
                product['product_price'] = doc['final_price']
                
                product['product_category'] = productCategory
                
                product['product_website_name'] = "Trade-Mark"

                # append the product dictionary in the new list
                products.append(product)
        
        
            #products is a list of product dictionaries
            #remember how link is [site, productCategory]
            #we'll use productCategory to to the products, because all the stuff from trade-mark.com/womens/jackets should be jackets
            #so dict will be {'jackets' : listOfJacketProdcuts, ... }
            product_dict[productCategory] = products
        return product_dict