# -*- coding: utf-8 -*-
from connection import ScrapeBase


class SiteMethods( ScrapeBase ):
    """
    Global site methods to Filter against tags locating product category tags  
    """
    def __init__( self, html_tag, *args, **kwargs ):
        super(SiteMethods, self).__init__( *args, **kwargs )
        
        # Returns an empty array if  html_tag cannot be found
        
        self.html_tag = html_tag

  
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
            
 
if __name__=="__main__":

    categoriesClass = SiteMethods(div).filterTags('ul','http://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/')
    # categoriesProductsClass = Hawthorn().getProducts(categoriesClass)

    # out = open("output_files/hawthorn.txt", 'w')
    # out.write(json.dumps(categoriesProductsClass))

    print categoriesClass

    # print categoriesClass
    # print categoriesProductsClass     

   