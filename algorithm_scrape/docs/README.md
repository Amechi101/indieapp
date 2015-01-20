Application Overview (v1 Beta)
===================
The main goal is to build a fashion web scrapping application as a powerful resource to allow users to discover new hard to find websites or websites with a strong collective of independent designers specifically targeting products from these **independent designers**. Giving the user an app that groups these websites, designers and products in one easy to find place. Giving constant updates on new products they like from particular websites they choose to follow. As well alert users when new sites are added to the app. The user can share items they like anytime  throughout their social media platforms. As well see the items they've like on an engaging and beautifully built timeline. The app is meant to strongly focus on engaging users with designers products. learn more about a designers story/background and proliferate the sales of the designers products with features targeting around these notions, meaning less on the social aspect between **user to user** and more **user to designer**.

- The platform will find Men's & Women's Products

- Keywords for this app: Consumer Facing, Discoverability,  Content Curation, Web Scrapping, Fashion-Technology, Ecommerce, Retail, B2C

- New Name for the project is: ''

Django Data Models in respect to scrapping
===================
```
class Product(models.Model):
    product_name = models.CharField()
    product_price = CurrencyField()
    product_slug_url = models.URLField()
    product_category = models.CharField()
    product_image = CloudinaryField()
    product_website_name = models.CharField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
    active = models.BooleanField()
    **website = models.ForeignKey()**

class Website(models.Model):
    name = models.CharField()
    description = models.TextField()
    website_slug = models.SlugField()
    site_logo_image = CloudinaryField()
    menswear = models.BooleanField()
    womenswear = models.BooleanField()
    active = models.BooleanField()
    date_added = models.DateTimeField()
    last_modified = models.DateTimeField()
```
Scrape Algorithm
=============
write below
Registered Website Id's
===================
> name_of_website = website_id

Maison Kitsune = 1
Hotel 1171 = 2
Nu* New York = 3
Project No.8 = 4
Miss Hoe = 5
Reformation = 6
Trade-Mark = 7


Registering a website for products to be viewed
==============

1. Add a "website" to the website model in the django admin area. Initially the field(s) `active`  will be **detonated with no checkmark** and  `website slug` field will be left **blank**. Indicating the current registered "website" has a status of **In-Process**  and the "website" is being tested for scrapping products using the `Scrape Algorithm`. Moreover, you should see the id value for the website in the breadcrumb right above ( Change Websites ) **Home › Website › Websites › website_id **. This will be the value used in Step **2.** to match the "website" with the correct products in the db when we scrape the items.
 
2. Next create a `_websitename_views.py` file in `scrap` directory in Django for the registered "website" being scrapped.  Import the methods DataCompiler() and Website_name() from the `Scrape Algorithm`,  into the `_websitename_views.py` file. See algorithm_scrape/docs/`_websitename_views.py` in github for a skeleton file and detailed instructions for this step inside. After setting up the view add these lines of code below (with the specific information for the site ) in scrap/`urls.py` 
```
from scrap._websitename_views.py import function_name_from_view

url(r'^_internal/websitename_api/', function_name_from_view),
```
*Do not add any underscores or dashes to websitename. It should be all undercase letters and no spaces e.g. trademark, zara, reformation.

3. We now setup a cron job to the API link to call and scrape the site every XX-day at XX:XX time. To get new products or update any fields that may have changed on the products. On the front-end if users are  signed up with our app they get a email notifications when we get new products for a particular "website" **(They Follow Only)**. This happens only when after we scrap and the "website" they follow gets a new instance of products stored in the db.