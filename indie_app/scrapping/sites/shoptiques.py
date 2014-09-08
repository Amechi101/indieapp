from bs4 import BeautifulSoup
import urllib2
import requests

def httpGet(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    
    req = urllib2.Request(url, headers = headers)
#========= try catch not working to handle HTTP Error 500 ==============
    try:
        connection = urllib2.urlopen(req)
    except urrlib2.HTTPError:
        connection = "None"
        
    #print url + ": " + str(connection.getcode())
    return connection.read()

def getCategories():
    categories = [

    ["Dresses", "http://www.shoptiques.com/categories/clothing/dresses"], 
    ["Tops","http://www.shoptiques.com/categories/clothing/tops"], 
    ["Bottoms","http://www.shoptiques.com/categories/clothing/bottoms"], 
    ["Jumpsuits & Rompers", "http://www.shoptiques.com/categories/clothing/jumpsuits-and-rompers"], 
    ["Jackets & Blazers", "http://www.shoptiques.com/categories/clothing/jackets-and-blazers"], 
    ["Outerwear", "http://www.shoptiques.com/categories/clothing/outerwear"], 
    ["Swimwear", "http://www.shoptiques.com/categories/clothing/swimwear"], 
    ["Intimates","http://www.shoptiques.com/categories/clothing/lingerie"]

    ]
    return categories

def getProducts(site):
    toReturn = []
    
    html =httpGet(site)
    soup = BeautifulSoup(html)
    div = soup.find('div', class_="products")
    if (div is None):
        return []
    products = div.find_all('div', class_="productImageHolder")
    counter = 0
    prices = soup.find_all('p',class_='price')
    for product in products:
        link = product.find('a')
        url = "http://www.shoptiques.com/" + link.get('href')
        #print url
        name = link.find('img').get('title')
        #print name
        img_url = link.find('img').get('src')
        #print img_url
        
        price = prices[counter].text.strip()
        #print price
        counter = counter + 1
        designer = getDesigner(url)

        toReturn.append([str(name), str(url), str(img_url), str(price), designer])
    #print toReturn
    return toReturn 

def getDesigner(url):
    #url = "http://www.shoptiques.com/" + url
    if (url != "http://www.shoptiques.com//products/slouchy-sweaterpants"):
        soup = BeautifulSoup(httpGet(url))
        try:
          brand = soup.find("span", itemprop="brand").text.strip()
        except AttributeError:
          brand = "None"
        return str(brand)
    return "None"




if __name__=="__main__":
    categories = getCategories()
    results = {}
    for cat in categories:
        results[cat[0]] = getProducts(cat[1])
        print cat[0]
    print results

        
