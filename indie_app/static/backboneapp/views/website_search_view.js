"use strict";

/*
 *
 *@title View for all websites
 *@description creating/deleting search tags, updating search count & collection based on search tags
 *@intial_view with all the sites loaded upfront to search
 */


var websiteSearchView = Backbone.View.extend({
    //this --> websiteSearchView scope
    el:'#nav-filters',
    list_tags_tpl: _.template($('#listTagTemplate').html()),
    events: {
        "click .list-tags .close a": "remove_filter"
    },
    initialize: function() {
        _.bindAll(this,'render','filter_tags','model_count','init_filters','website_list');
        this.filters = {};  
        
        this.model_count();
        this.filter_tags();
        this.init_filters();
        
        this.websiteView = new websiteView({collection: new websiteSearchCollection(this.collection.models)});
        this.render();


    },
    model_count:function() {

        $('#websites-count strong', this.el)
            .attr('data-filter',  this.collection.models.length )
            .text(this.collection.models.length.toString());
    },
    init_filters: function ( ) {
        var self = this; 
            
        var createListTags = $('.list-tags', this.el);

        // console.log($('.search-filter-container li'));
        $('.search-filter-container li').each(function( index ) {
            var _this = this;
            var filter =  $(_this).data("filter");

            // console.log(filter);
            
            $(_this).on( 'click', function() {
                self.filters[$(_this).data("filter-type")] = filter;
                self.render();
            });    
        });

    },
    filter_tags: function() {

        var searchTerms = {
            sex: ['Menswear','Womenswear'],
            trending:['1 Week Ago','3 Weeks Ago','+ 1 Month Ago']
        }

        // Looping construct to add <li> tags.
        for (var i= 0; i < searchTerms.sex.length; i++) {
            $('#website-sex', this.el).append('<li data-filter-type="sex" data-filter="' + searchTerms.sex[i] + '">' + searchTerms.sex[i] + '</li>'); 
        }


        for (var k=0;  k < searchTerms.trending.length; k++) {
            $('#website-trending', this.el).append('<li data-filter-type="trending" data-filter="' + searchTerms.trending[k] + '">' + searchTerms.trending[k] + '</li>');
        }
      
    },
    remove_filter: function(event) {
        var filter_type = $(event.target).data("filter-type");
        delete this.filters[filter_type];
        this.render();
    },
    website_list:function() {
        var self = this; 
        var filtered_websites = self.collection.filter(function(website) {
            var keep = true;
            $.each(self.filters, function(ftype, fvalue) {
                if(ftype == "sex") {
                    if(!website.get(fvalue.toLowerCase()))
                        keep = false;
                } else if(ftype == "age") {
                    // check site date here
                }
                // generic logic not useful here but might be for another page
                else if(website[ftype] != fvalue) {
                    //keep = false;
                }
            });
            return keep;
        });
        this.websiteView.collection.reset(filtered_websites);
    },
    render: function() {
        
        var self = this;

        //List Tags
        $('.list-tags').html(self.list_tags_tpl({tags: self.filters}));
        this.website_list()
    }
});


/*
 *
 *@title View for a websites
 *@description To display the products based on the search tag filters
 *@initial Loads all of the sites upfront (with pagination) to allow for user
 */
var websiteView = Backbone.View.extend({
    //this is the scope of the Backbone selector, choosing the descendants of the
    initialize: function () {
        this.listenTo(this.collection, "reset", this.render);
    },
    el:'#sidebar_search_block',
    template: _.template($('#websiteTemplate').html()),
    render: function() {
        this.$el.html(this.template({websites: this.collection.models}));
    }
});


var websiteSearchViewObject = new websiteSearchView({collection:websitesCollection}); 

// console.log(websiteSearchViewObject);

/*
 *
 *
 * NEXT STEPS
 *
 */

// @TODO Is to bind the list tags, to the events in the other function (website_list), so when a specific list tag is 
// choosen it filters out the sites based on the tag and if a list tag is destroyed (removed) then it restores that back to the 
// state based on what filter tag is left. If no tags then all sites are loaded but if no query is found with the tags returns an empty div
//  saying no items are available.



