"use strict";

var websiteSearchView = Backbone.View.extend({
    //this is the scope of the Backbone selector, choosing the descendants of the
    el:'.wrapper-nav',

    initialize: function() {
        _.bindAll(this,'render','search_categories','model_count','filter_sex');
      
        this.render();
    },
    model_count:function() {
        console.log(this.model.models);

        $('#websites-count strong', this.el)
            .attr('data-filter',  this.model.models.length )
            .text(this.model.models.length.toString());
    },
    filter_sex: function ( ) {
        
        this.model_count();

        var createListTags = $('.list-tags', this.el);

        console.log(createListTags.find('li a').text() > 0 )

        $('#website-sex li', this.el).each(function( index ) {
            var _this = this;
            var filter =  $(_this).data("filter");
            
            

            
            $(_this).on('click', function() {
                var filteredItems = _.filter( [filter], function (i) {
                   

                    switch(i) {
                        case "Womenswear": 
                            if( createListTags.find('li a').text() > 0 ) {
                               
                                createListTags.find('li').remove()
                            } else {
                                createListTags.append('<li class="close style2"><a href="javascript:void(0)">' + i + '</a></li>');
                            }
                            
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
        this.filter_sex();
    }
});

//View Dropdown
var websiteSearchViewObject = new websiteSearchView({model:websitesCollection}); 

console.log(websiteSearchViewObject);