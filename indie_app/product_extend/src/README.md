Application Overview
================

The main goal of the application is to build a fashion web scrapping engine as a powerful resource for users search from specific sites to find the latest and greatest products from **independent designers**. 

- The platform will find Men's & Women's Products

- New Name for the project is: 'Indiescrap'

The application is separated by a few areas and interactions:

**Backend interactions**

- Scrapping the product(s) --> **Scrap & Ingestor Phase**
- Saving the product(s) --> **Scrap & Ingestor Phase**
- Sending signal to users when we scrap a new site or new products are available from any site we scrap --> **Scrap & Ingestor Phase**
- Searching Python Model for product(s) --> **User Interaction *Product Filter**
- Addding and Deleting likes from User Model for product(s) --> **User Interaction *Timeline**

**Frontend interactions**
- Filtering the product(s) --> **User Interaction *Product Filter**
- Liking the product(s) --> **User Interaction *Timeline**
- User viewing liked product(s) --> **User Interaction *Timeline**
- User filtering their timeline --> **User Interaction *Timeline**

"Scrap & Ingestor Phase" 
----------------
** Information retrievel and storage within the python model abstraction (DB)**


- Phase I:

```
Base Class:
Access the website headers, make a HTTP connection and initialize the beautiful   soup module

getHttp():
getSoup():
```
- Phase 2

```
Site Class:
Specific methods to scrap each site and retrieve all required information 
required for the database. We search by [ u'CategoryUrl', [u'ProductCategoryName'] 

Has two required methods:

getCategoryLinks():
getProducts():

Things we are aiming to get:
Product = {}
-  product['name'] = Name_Of_Product
-  product['product_url'] = Product_URL_Specific
-  product['img'] = Product_Image
-  product['price'] = Product_Price
-  product['designer_name'] = Who_Created_The_Product
-  product['website_home_url'] = Site_We_Are_getting_Items_From
-  product['name_of_brand'] = Name_Of_The_Specific_Brand
-  product['Category'] = Category_Of_The_Specific_Product

```

- Phase 3

```
Compiler Class:

Compiles all information from the Site Classes into JSON objects and converts it into a python object

Has two required methods:

runSiteScript()
getJsonData()

```

- Phase 4

```
This phase requires the action of the Dict Class, in which the program will access the structure that will be compiled into: 

Python_Object = { 
        'Website': { 
                'product_category' : [.... ]
format inside product_category --> [0] = { 'name' : 'leather jacket', 'url' : ...}
    }
}

Dict Class:

The Dict Class will be the main module to find, sort, delete and add any new values to Django Model. The main purposes of this class will be sorting thru the dictionary structure from the Compiler Class and finding information  pertaining to the matched fields on the Django and running methods against the model. 

Has 'x' required methods:

TBD!!

```
```
Signal Class:

This will send signals to the user when we scrap a site only when, the Dict class returns a new instance of a product created by scrapping or we add a new website for scrapping into our program.

Has 'x' required methods:

TBD!!

```
"User Interactions" 
----------------
** User based events the send signals to the (DB), to the scrapping program or generate other events**


> Timeline: An area on the user dashboard for viewing and filtering of their liked items on the site. 

Front-End:

- Liking the product(s) --> **User Interaction *Timeline**
- User viewing liked product(s) --> **User Interaction *Timeline**
- User filtering their timeline --> **User Interaction *Timeline**

When the user likes a product the item appears on their timeline within their dashboard. Where the user may filter via Month & Year to find a particular set of images liked in the past. The default view will be the current month and year selection of photos.

Back-End:

- Addding and Deleting likes from User Model for product(s) --> **User Interaction *Timeline**

The user will be able to add likes (when liking item) and delete likes when on their timeline. The item will then be wiped from memory in their accounts.

------
> Product Filter: An area on the product page for users to filter through the site based on set filter parameters

Front-End:

- Filtering the product(s) --> **User Interaction *Product Filter**

Back-End:

- Searching Python Model for product(s) --> **User Interaction *Product Filter**


