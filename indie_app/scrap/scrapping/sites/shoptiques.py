from bs4 import BeautifulSoup
from datetime import timedelta
import urllib2
import requests
import re
import json


class Shoptiques( object ):

    def __init__( self ):
        pass

    def httpGet( self, url ):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        #print "in get method " + url
        req = urllib2.Request(url, headers = headers)
    #========= try catch not working to handle HTTP Error 500 ==============
        try:
            connection = urllib2.urlopen(req)
        except urllib2.HTTPError:
            connection = "None"
            
        #print url + ": " + str(connection.getcode())
        return connection.read()

    def getCategories( self ):
        categories = [["Dresses", "http://www.shoptiques.com/categories/clothing/dresses"], ["Tops","http://www.shoptiques.com/categories/clothing/tops"], ["Bottoms","http://www.shoptiques.com/categories/clothing/bottoms"], ["Jumpsuits & Rompers", "http://www.shoptiques.com/categories/clothing/jumpsuits-and-rompers"], ["Jackets & Blazers", "http://www.shoptiques.com/categories/clothing/jackets-and-blazers"], ["Outerwear", "http://www.shoptiques.com/categories/clothing/outerwear"], ["Swimwear", "http://www.shoptiques.com/categories/clothing/swimwear"], ["Intimates","http://www.shoptiques.com/categories/clothing/lingerie"]]
        return categories

    def getDesigner( self, url ):
        #url = "http://www.shoptiques.com/" + url
        if (url != "http://www.shoptiques.com//products/slouchy-sweaterpants"):
            soup = BeautifulSoup(self.httpGet(url))
            try:
              brand = soup.find("span", itemprop="brand").text.strip()
            except AttributeError:
              brand = "None"
            final_string = ""
            try: 
                return str(brand)
            except:
                return brand
        return "None"

    def getProducts( self, site ):
        toReturn = []
        html = self.httpGet(site)
        soup = BeautifulSoup(html)
        breakout = False
        next_page = "none yet"

        # Time check for script 
        duration = timedelta(seconds=60)
        while not breakout:
            products = soup.find_all("div", { "class" : "product with-swatches listproduct" , "class": "product with-swatches end listproduct" })
            for product in products:
                link = product.find('a')
                url = "http://www.shoptiques.com/" + link.get('href').strip()
                name = link.find('img').get('title')
                img_url = link.find('img').get('src')
                price = ""
                #print img_url
                try:
                    price = product.find("span", "retail").text.strip()
                except AttributeError: 
                    price = product.find('p', class_= 'price').text.strip()      
                    

            #========== runtime changes drastically with call to get designers ==================
                designer = self.getDesigner(url)
                #designer = getDesigner(url)
                toReturn.append([str(name), str(url), str(img_url), str(price), designer])
            try:
                next_page = "http://www.shoptiques.com" + soup.find('div', class_='pages').find('a', class_='nextLink').get('href').strip() 
                print next_page
                html = self.httpGet(next_page)
                soup = BeautifulSoup(html)
            except:
                breakout = True
        return toReturn 

if __name__=="__main__":
    scrapped_site = Shoptiques()
    categories = scrapped_site.getCategories()
    results = {}
    
    for cat in categories:
        results[cat[0]] = scrapped_site.getProducts(cat[1])
        print cat[0]
    print results
    out = open("shoptiques.txt", 'w')
    out.write(json.dumps(results))
        #file.close()

    #    http://www.shoptiques.com/categories/clothing/dresses?category=16&max=90&c=productList&a=list&offset=180

    # everything until ? 
    # max until index value of first &
    # &
    # offset until end

    #get the last number of the offset and search through all of the links until the larger than the current offset
    #<a href="/categories/clothing?category=1&amp;max=90&amp;c=productList&amp;a=list&amp;offset=90" class="nextLink" data-offset="90">&gt;</a>
    #  .find('a', class_='nextLink')
            
