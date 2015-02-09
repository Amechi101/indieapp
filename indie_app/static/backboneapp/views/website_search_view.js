"use strict";

/*
 *
 *@title View for all websites
 *@description creating/deleting search tags, updating search count & collection based on search tags
 *@intial_view with all the sites loaded upfront to search
 */


var websiteSearchView = Backbone.View.extend({
    //this is the scope of the Backbone selector, choosing the descendants of the
    el:'#nav-filters',
    list_tags_tpl: _.template($('#listTagTemplate').html()),
    initialize: function() {
        _.bindAll(this,'render','search_categories','model_count','init_filters');
        this.filters = {};  
        this.search_categories();
        this.init_filters();
        this.render();
    },
    model_count:function() {
        // console.log(this.model.models);

         this.collection.each(function(website){
            console.log(website);
        });


        $('#websites-count strong', this.el)
            .attr('data-filter',  this.collection.models.length )
            .text(this.collection.models.length.toString());
    },
    init_filters: function ( ) {
        var self = this; 
        this.model_count();

        var createListTags = $('.list-tags', this.el);

        console.log($('.search-filter-container li'));
        $('.search-filter-container li').each(function( index ) {
            var _this = this;
            var filter =  $(_this).data("filter");
            
            $(_this).on('click', function() {
                self.filters[$(_this).data("filter-type")] = filter;
                self.render();
            });    
        });

    },
    search_categories: function() {

        var searchTerms = {
            sex: ['Menswear','Womenswear', 'Both'],
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
    render: function() {
        var self = this;
        var filters = Object.keys(this.filters).map(function(key){
                return self.filters[key];
        });
        $('#list-tags').html(this.list_tags_tpl({tags: filters}));
    }
});


/*
 *
 *@title View for a websites
 *@description 
 *
 */
var websiteView = Backbone.View.extend({
    //this is the scope of the Backbone selector, choosing the descendants of the
    el:'#indie-populate-websites',

    initialize: function() {
        _.bindAll(this,'render');
      
        this.render();
    },
    template: _.template($('#websiteTemplate').html()),

    render: function(){

        this.collection.forEach(function(element) {
            console.log( element.attributes.fields)

        });
        
    }
});


var websiteSearchViewObject = new websiteSearchView({collection:websitesCollection}); 
var websiteViewOject = new websiteView({ collection:websitesCollection });

console.log(websiteSearchViewObject);
