from base import ScrapeBase

# import urllib2
# import json

class Hawthorn( ScrapeBase  ):

    def __init__(self):
        pass


    def getCategoryLinks( self ):
        """
        This method retrieves category links from the homepage and saves them in this format [ u'category_url', [u'productCategory_name'] ]
        """
        def filterTags( html_tag ):

            ul_tag = [ x for x in html_tag.descendants if x.name == 'ul' ] #Finding ul within descendants
            ul = ul_tag[0] #Getting on the first ul
            
            return [ [x.get('href'), x.contents] for x in ul.find_all('a') if x.get('href').strip().startswith("http://www.hawthornboutique.com/product-categories/")]
           
       
        # This is the container we are searching against
        divs = list([ x for x in ScrapeBase().getSoup("http://www.hawthornboutique.com").find_all('div') if x.get('class') == [u'content-width'] ])[2:3]
        
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
                products = ScrapeBase().getSoup(link[0]).find_all('article', class_="column product")
            elif products:
                products = []
                
            # To add the product information that will be
            # dictionary item_name: ProductInformation items inside a new list
            productsList = []
           
            for item in products:
            
                product = {}

                # Geting information from within a tag
                hawthron_product_atag = item.find('a')
                
                product['name'] = hawthron_product_atag.get('title')

                product['product_url'] = hawthron_product_atag.get('href')

                product['img'] = hawthron_product_atag.find('img').get('data-lazy-load')

                try:
                    product['price'] = item.find('span', itemprop = "price").contents[0]
                except AttributeError: 
                    return 0
                
                #Designers are in the title of the product name
                #but not constant enough to scrap in completion, so we must manually add
                #the designers to each product or figure a method to extract each name
                # for the product being scrap
                product['designer_name'] = 'None'

                # Must figure methods to get this information automatically instead of manually writing these two values
                # for every site we scrap
                product['website_home_url'] = "http://www.hawthornboutique.com"
                product['name_of_brand'] = "Hawthorn"

                # append the product dictionary in the new list
                productsList.append(product)

        
            #products is a list of product dictionaries
            #remember how link is [u'site', [u'productCategory']]
            #we'll use productCategory to the products.
            #so dict will be {'jackets' : listOfJacketProdcuts, ... }
            product_dict[link[1][0]] = productsList
        return product_dict

    

 
# if __name__=="__main__":

#     categoriesClass = Hawthorn().getCategoryLinks()
#     categoriesProductsClass = Hawthorn().getProducts(categoriesClass)

#     out = open("output_files/hawthorn.txt", 'w')
#     out.write(json.dumps(categoriesProductsClass))

#     print categoriesProductsClass.keys()

#     # print categoriesClass
#     # print categoriesProductsClass

    