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

    initialize: function() {
        _.bindAll(this,'render','search_categories','model_count','filter_sex_tag');
      
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
    filter_sex_tag: function ( ) {
        
        this.model_count();

        var createListTags = $('.list-tags', this.el);


        $('#website-sex li', this.el).each(function( index ) {
            var _this = this;
            var filter =  $(_this).data("filter");
            
            $(_this).on('click', function() {
                var filteredItems = _.filter( [filter], function (i) {
                   
                    switch(i) {
                        case "Womenswear": 
                            createListTags.append('<li class="close style2"><a href="javascript:void(0)">' + i + '</a></li>');
                        break;

                        case "Menswear": 
                            createListTags.append('<li class="close style2"><a href="javascript:void(0)">' + i + '</a></li>');
                        break;

                        case "Both": 
                            createListTags.append('<li class="close style2"><a href="javascript:void(0)">' + i + '</a></li>');
                        break;
                    }

                    
                });
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
            $('#website-sex', this.el).append('<li data-filter="' + searchTerms.sex[i] + '">' + searchTerms.sex[i] + '</li>'); 
        }


        for (var k=0;  k < searchTerms.trending.length; k++) {
            $('#website-trending', this.el).append('<li data-filter="' + searchTerms.trending[k] + '">' + searchTerms.trending[k] + '</li>');
        }
      
    },
    render: function() {
        this.search_categories();
        this.filter_sex_tag();
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