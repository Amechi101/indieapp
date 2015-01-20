// @TODO To design with the tastypie api to filter and generate dropdown search list (with cancelable componenets) and search filter for the entire site with 
// all functionality attached in this JS file. For: Collection. Views. and Model.


/*
 *
 * Backbone Model ( returing URL from tastypie link and craeting the list defaults for the dropdown on the search page)
 *
 */

var websiteSearchModel = Backbone.Model.extend({
    initialize: function() {
    },
    defaults :{
        categories:{
            letter:['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
            trending:['Newest sites','Oldest sites'],
            sex:['Menswear','Womenswear']
        }
    }
});


/*
 *
 * Backbone Collection ()
 *
 */
var websiteSearchCollection = Backbone.Collection.extend({
    
    model:websiteSearchModel,
    url:'http://127.0.0.1:8000/scrap_api/_internal_websiteall_api/v2/all_wesbsites/'

});


/*
 *
 * Backbone View ( Rendering the defaults of the model )
 *
 */
var dropdownSearchView = Backbone.View.extend({
    //this is the scope of the Backbone selector, choosing the descendants of the
    el:'.wrapper-nav',

    initialize: function() {
        _.bindAll(this,'render','filterFunc');
      
        this.render();
    },
    events: {
    },
    filterFunc: function() {
        //Array to access the information from the backbone models
        var searchFilterItems = [this.model.attributes.categories.letter, this.model.attributes.categories.trending, this.model.attributes.categories.sex];

      
        // Looping construct to add the elements from the model in a <li> tag.
        for (var i = 0, j=0, k=0; i < searchFilterItems[0].length || j < searchFilterItems[1].length || k < searchFilterItems[2].length; i++, j++, k++) {
        
            //letter filter
            if ( i < searchFilterItems[0].length ) {
              $('#letter', this.el).append('<li>' + searchFilterItems[0][i] + '</li>');  
            }

            //trending filter
            if ( j < searchFilterItems[1].length ) {
              $('#trending', this.el).append('<li>' + searchFilterItems[1][i] + '</li>');
            }
            
            //sex filter
            if ( k < searchFilterItems[2].length ) {
              $('#sex', this.el).append('<li>' + searchFilterItems[2][i] + '</li>');
            }

        }
      
    },
    render: function() {
        this.filterFunc();
    }
});

//Model
var websiteSearchModelObject = new websiteSearchModel();

//Collection
var websiteSearchCollectionObject = new websiteSearchCollection();

//View Dropdown
var searchViewObject = new dropdownSearchView({model:websiteSearchModelObject}); 

// console.log(websiteSearchModelObject);
// console.log(websiteSearchCollectionObject);

