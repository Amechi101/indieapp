from base import SearchBase

import urllib2
import json
import pprint


class TrademarkScrape( SearchBase ):


    def getDivs(self):
        self.soup(urllib2.urlopen("http://www.trade-mark.com").read()) # passes html to soup

        # finds all <div class="nav"> place in array
        divs = [ x for x in self.soup.find_all('div') if x.get('class') == [u'nav'] ] 

        return self.getLinks(divs[0]) #There should only be one <div class="nav"> at trade-mark.com, so we'll pass this tag over to getLinks


    def getLinks(self, div):
        uls = [x for x in div.children if x.name == 'ul'] # iterate through the children of div, and add them to uls if its a <ul ...
        ul = uls[0] #There should only be one
        
        lis = list([x for x in ul.children if x.name == 'li'])[:2] # first two li elements of the ul element have the "women" and "men" category

        womensLi = lis[0] #The first li is of the women category. TODO add mens
        nav_dropDown = womensLi.div
        
        # return [[link, name], [link, name]....] by finding all links: find_all('a'), only if the link goes to a trademark site.
        return [[x.get('href'), x.contents[0]] for x in nav_dropDown.find_all('a') if x.get('href').startswith("http://www.trade-mark.com/womens/")] #Yes, this is only womens. TODO mens
    


    def getProducts(self, links):
        dict = {} # a new dictionary
        
        for link in links:
            link[0] = str(link[0]) # link is [site, productCategory], but site is unicode object. Convert it to a string
            print link[0]
            
            if link[0].strip() == r'http://www.trade-mark.com/womens/summer.html': 
                continue  #Skip womens/summer.html. Has no products.
           
            html = urllib2.urlopen(link[0]).read() # read the html from this url
            
            
            
            #This is the tricky part. Simply getting the html from the site won't work.
            # The site has this in it: <div class="listing-products listing-products-alt clearfix"> </div>
            #But later, javascript runs and fills it in. Each site has an 'cat_id', and the javascript passes this id to www.trade-mark.com/solr,
            #which returns json
            
            index = html.index("var cat_id") + len("var cat_id") + 3
            html = html[index:]
            html = html[1:html.index(";")-1]
            
            #html now is the said id

            rsp =  urllib2.urlopen("http://www.trade-mark.com/solr/?q_is_in_stock=true&q_category_ids=" + html + "&rows=10000&fl=name,url,price,final_price,sale_price,product_id,image_varchar,alt_image_varchar,color_gpd,parent_id_int&sort=cat_" + html + "_co+asc").read()
            
            #this call gets the responce from www.trade-mark.com/solr, using the id we have acquired

            #load this json to a python dictionary
            httpDict = json.loads(rsp)
            docs = httpDict['response']['docs']
            
            #The following for loop copies the data from httpDict into products
            products = []
            for doc in docs:
                product = {}
                if 'image_varchar' in doc: product['img1'] = doc['image_varchar']
                else:  print('Missing image_varchar')

                if 'name' in doc: product['name'] = doc['name']
                else:  print('Missing name')

                if 'url' in doc:
                    product['url'] = doc['url']
                    #product['description'] = self.getDescription(doc['url'])
                    #This is commented out because its not ready yet, but it should scrape the description from the url and put it in product['description']

                else:  print('Missing url')

                if 'alt_image_varchar' in doc: product['img2'] = doc['alt_image_varchar']
                else:  print('Missing alt_image_varchar')

                if 'final_price' in doc: product['final_price'] = doc['final_price']
                else:  print('Missing final_price')
                

                products.append(product)
        
        
            #products is a list of product dictionaries
            #remember how link is [site, productCategory]
            #we'll use productCategory to to the products, because all the stuff from trade-mark.com/womens/jackets should be jackets
            #so dict will be {'jackets' : listOfJacketProdcuts, ... }
            dict[link[1]] = products
        return dict


if __name__ == "__main__":
    
#    pp = pprint.PrettyPrinter(indent=4)
#    pp.pprint ((TrademarkScrape().getDetails(urllib2.urlopen("http://www.trade-mark.com/newport-jacket-1.html").read())))
#    exit()
#    

    links = (TrademarkScrape().getDivs())
    pp = pprint.PrettyPrinter(indent=4)
    
    out = open('out.txt', 'w')
    dict = (TrademarkScrape().getProducts(links))
    out.write(json.dumps(dict))
    print dict.keys()
    print ("\n\nResults are in out.txt")
    print ("Load the results back into python with:")
    print ("\n\nimport json")
    print ("fin = open('out.txt', 'r')")
    print ("txt = fin.read()")
    print("fin.close()")
    print ("results = json.loads(txt)")

    print ("""results is a dictionary of lists of dictionaries
        results
            'jackets' : [.... ]
            'dresses' : [.... ]
                        [.... ] 
                            [0] = { 'name' : 'leather jacket', 'url' : .........}
                """)



