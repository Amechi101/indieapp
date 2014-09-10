import urllib2
from bs4 import BeautifulSoup
import json

class Hawthorn ( object ):

    def __init__( self ):
        pass

    def httpGet(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        
        req = urllib2.Request(url, headers = headers)
        
        connection = urllib2.urlopen(req)
        print url + ": " + str(connection.getcode())
        return connection.read()

        # You can just ignore the headers and req stuff don't exist, but for some reason it won't work without them
        # http://stackoverflow.com/questions/13303449/urllib2-httperror-http-error-403-forbidden



    def getCategories(self):
        
        html = self.httpGet("http://www.hawthornboutique.com/products-page")

        soup = BeautifulSoup(html)
        menu = soup.find('ul', class_="menu")
        lis = [x for x in menu if x.name is not None]
        return [x.contents[0].get('href') for x in lis if x.contents[0].get('href').strip().startswith("http://www.hawthornboutique.com/product-categories/")]

    def getProducts(self, site):
        toReturn = []
        
        html =self.httpGet(site)
        soup = BeautifulSoup(html)
        div = soup.find('div', class_="columns four")
        if (div is None):
            return []
        products = div.find_all('article')
        for product in products:
            link = product.find('a')
            url = link.get('href')
            name = link.get('title')
            img_url = link.find('img').get('src')
            price = product.find('span', itemprop = "price").contents[0]
            toReturn.append([name, url, img_url, price, self.getDetails(url)])
        return toReturn

    def getDetails(self, url):
        soup = BeautifulSoup(self.httpGet(url))
        div = soup.find('div', itemprop="description")
        try:
            return div.find('p').contents[0].strip()
        except AttributeError:
            return None

if __name__=="__main__":
    scrapped_site = Hawthorn()
    categories = scrapped_site.getCategories()
    print categories
    results = {}
    for category in categories:
        results[category] = scrapped_site.getProducts(category)
    out = open("hawthorn.txt", 'w')
    out.write(json.dumps(results))
