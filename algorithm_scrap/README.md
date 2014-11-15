Application Overview (v1 Beta)
====================

--------------------------------------------------
The main goal of the application is to build a fashion web scrapping engine as a powerful resource for users to search from specific sites to find the latest and greatest products from **independent designers**. 

- The platform will find Men's & Women's Products

- New Name for the project is: 'Indiescrap'

The application is separated by a few areas and interactions:

**Backend interactions**

- Scrapping the product(s) --> **Scrap & Ingestor Phase**
- Saving the product(s) --> **Scrap & Ingestor Phase**
- Sending signals to users when we scrap a new site or new products are available from any site we scrap --> **Scrap & Ingestor Phase**
- Searching Python Model for product(s) --> **User Interaction *Product Filter**
- Addding and Deleting likes from the User Model for product(s) --> **User Interaction *Timeline**

**Frontend interactions**
- Filtering the product(s) --> **User Interaction *Product Filter**
- Liking the product(s) --> **User Interaction *Timeline**
- User viewing liked product(s) --> **User Interaction *Timeline**
- User filtering their timeline --> **User Interaction *Timeline**

"Scrap & Ingestor Phase" 
----------------
** Information retrievel and storage within the python model abstraction (DB)**

-------------------------------------------

- Phase I:

```
Base Class:
Access the website headers, make a HTTP connection and initialize the beautiful soup module

Required methods:
-----------------
getHttp():
    returns the the site headers and access the site for each site we scrap

getSoup():
    returns the Beautiful Soup methods and gives use access to the API using the site we get from getHttp()
```
- Phase 2

```
Site Class:
Specific methods to scrap each site and retrieve all required information 
required for the database.

Required methods:
-----------------
getCategoryLinks():
    returns the values [ u'CategoryUrl'], [u'ProductCategoryName'] 

getProducts():
    finds the product based on what getCategoryLinks() returns
    Product = {}
    -  product['name'] = Name_Of_Product
    -  product['product_url'] = Product_URL_Specific
    -  product['img'] = Product_Image
    -  product['price'] = Product_Price
    -  product['designer_name'] = Who_Created_The_Product
    -  product['website_home_url'] = Site_We_Are_getting_Items_From
    -  product['name_of_brand'] = Name_Of_The_Specific_Brand
    -  product['Category'] = Category_Of_The_Specific_Product
    
    
> Additional Procedures

Create error blocks on each of the site methods throughout the program to catch important errors we may run into while scrapping through the site before moving into saving and or after saving the information.
```

- Phase 3

```
SQL Alchemy Classes:

From each of the scrapping methods from each individual Site Class we will store the items directly into the database. Re-Creating the models again in models.py ( within the algorithm_scrap module to match to the model rep). This Class also will be the main module to delete and/or update any new values to Django Product Model (database). 

> Additional Procedures

We will be running a cron job to allow for automated running of each scrap algorithm to run once a week on --------- at ------ AM/PM

Signal Class:

This will send signals to the user when we scrap a site only when, a new instance of a product from scrapping is signaled by the program or when we add a new website for scrapping at the Site Class level (Phase 2).

Has 'x' required methods:

TBD!!

```
"User Interactions" 
----------------
** User based events that send signals to the backend to do something or consume some sort of data**

-------------------------------------------------------------
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
> Product Filtering: For users to filter through the our products based using set filter parameters

Front-End:

- Filtering the product(s) --> **User Interaction *Product Filter**

Each site will have its predefined categories, i.e when you select a website those predefined categories will appear for filtering products for that particular site. You must select a particular site before being allowed to filter using categories.  

Filtering Logic:

- If the user selects a website from the homepage ( will be redirected to the product page ) and/or on the product page then:

1. The website filter shows the current site begin used (loading it from the database to display) changing the page's view loading the products for that specific site and

2. Filling the product filter with all the pre-loaded categories for   that particular website

3. The user will be able to on product page interact with the website filter to continuously change which website to shop on. Changing the view for aformentioned steps 1 through 2.

If the user selects `All` from the homepage ( will be redirected to the product page ) or from the website filter on the product page then they will be only able to filter using 
1. Price range 
2. Generic Filters
3. Newest Scrap 
4. Oldest Scrap 
5. Popular Scrap 

**Filtering Options:**
```
    - Websites (1 & Choice indepedent)
    - Categories ( Depends on 1 )
    - Price Range ( Choice indepedent )
    - Newest Scrap ( Choice indepedent )
    - Oldest Scrap ( Choice indepedent )
    - Popular Scrap ( Choice indepedent )
```
Back-End:

- Searching Python Product Model for product(s) using backbone.js to update views on front-end --> **User Interaction *Product Filter**

- Searching Python Product Model for categories(s) using backbone.js to update views on front-end --> **User Interaction *Product Filter**

"Access and Privilages" 
----------------
**User Defined Roles within the application**

--------------------------------------------------------

**Access Granted for Non-members**:
- Only Viewing and Browsing product information 

**Access Granted for Members**:
- Liking Products
- Dashboard Access:
  - Notifications on new products or new scrapped sites
  - Account Settings
  - Save liked products on personalized created timeline

