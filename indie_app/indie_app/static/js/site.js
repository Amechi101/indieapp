
/*

*--------------------------------------------------------------------*

Indie-Scrap interface design 

Copyright (C) 2014 Indie-Scrap 

*--------------------------------------------------------------------*

*/

"use strict";

//To avoid namespace collision
var indieScrapInitilazer =  indieScrapInitilazer || {};

indieScrapInitilazer = (function ( $, document, window, _ , undefined  ) {
    
    
    return {
        ProductFilter: function() {
          
            // var productFliter = Backbone.Model.extend({
            //     defaults :{
            //         categories:{
            //             // @TODO update logic to backend to change as to what site is currently being choosen by the user on the front-end
            //             // for men and women
            //             men:['Tops','Bottoms','Shorts','Jackets & Blazers','Sweaters','Outerwear','Shoes','Accessories','Undergarments'],
            //             women:['Dresses','Tops','Skirts','Shorts','Bottoms','Jumpsuits & Rompers','Jackets & Blazers','Sweaters','Outerwear','Shoes','Accessories','Lingerie']
            //         },
            //         priceRange:['0-50', '50-100','100-200','200-300','400+'],
            //         generalFilter:['Newest Scrap\'s','Oldest Scrap\'s','Popular Scarp\'s']
            //     };

            // });

            // var productView = Backbone.View.extend({
            //     //this is the scope of the Backbone selector, choosing the descendants of the
            //     el:'#product-navigation .filter-options',

            //     initialize: function() {
            //         _.bindAll(this,'render','filterFunc');
                  
            //         this.render();
            //     },
            //     filterFunc: function() {
            //         //Array to access the information from the backbone models
            //         var productFilterItems = [this.model.attributes.categories.men, this.model.attributes.categories.women, this.model.attributes.priceRange, this.model.attributes.generalFilter];
            //         var menuFilter = $('#men', this.el);
                  
            //           /*
            //             Looping construct to add the elements from the model in a <li> tag this will allow for easier access to attach any events and data 
            //             that needs to be transferred to the backend.

            //           */
            //         for (var i = 0, j=0, k=0, l=0; i < productFilterItems[0].length || j < productFilterItems[1].length || k < productFilterItems[2].length || l < productFilterItems[3].length ; i++, j++, k++, l++) {
                    
            //             //mens filter
            //             if ( i < productFilterItems[0].length ) {
            //               $('#men', this.el).append('<li id="' + productFilterItems[0][i] + '" class="product-options"><span></span>' + productFilterItems[0][i] + '</li>');  
            //             }

            //             //womens filter
            //             if ( j < productFilterItems[1].length ) {
            //               $('#women', this.el).append('<li id="' + productFilterItems[1][i] + '" class="product-options"><span></span>' + productFilterItems[1][i] + '</li>');
            //             }
                        
            //             //price filter
            //             if ( k < productFilterItems[2].length ) {
            //               $('#price', this.el).append('<li id="' + productFilterItems[2][i].replace('+','') + '" class="product-options"><span></span>$' + productFilterItems[2][i].replace('-', '-$') + '</li>');
            //             }

            //             // filter
            //             if ( l < productFilterItems[3].length ) {
            //               $('#other', this.el).append('<li id="' + productFilterItems[3][i].replace('+','') + '" class="product-options"><span></span>' + productFilterItems[3][i] + '</li>');
            //             }
            //         }
                  
            //     },
            //     render: function() {
            //         this.filterFunc();
            //     }
            // });
              
            // var productFliterObject  = new productFliter();
            // var productViewObject = new productView({model:productFliterObject});

            //     // console.log(productFliterObject)
            //     // console.log(productViewObject)
                

        }, 
        LeftGlobalSiteSearch: function() {


            /*
             *
             * Toggle functionality
             *
             */
            function SearchDropdown( element ) {
                this.el = element;
                this.initEvents();
            }

            SearchDropdown.prototype = {
                initEvents:function() {
                    this.el.on('click', function( event ) {
                        event.stopPropagation();
                        $(this).toggleClass('active');
                    });
                }
            };

            var searchByLetter = new SearchDropdown($('#global-site-letter'));
            var searchByTrending = new SearchDropdown($('#global-site-trending'));
            var searchBySex = new SearchDropdown($('#global-site-sex'));

            /*
             *
             * Backbone menu generator
             *
             */
            var websiteSearchModel = Backbone.Model.extend({
                defaults :{
                    categories:{

                        letter:['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                        trending:['Newest sites','Oldest sites'],
                        sex:['Menswear','Womenswear','Both']
                    }
                }
            });

            var websiteSearchView = Backbone.View.extend({
                //this is the scope of the Backbone selector, choosing the descendants of the
                el:'.wrapper-nav',

                initialize: function() {
                    _.bindAll(this,'render','filterFunc');
                  
                    this.render();
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
            
            var websiteSearchFliterObject = new websiteSearchModel();
            var searchViewObject = new websiteSearchView({model:websiteSearchFliterObject});
   
        },
        ProductMenuToggling:function() {
          
            /*
             *
             * Product Menu 
             *
             */
            var menuLink             = $('#menu-toggle'), //trigger for menu
                filterMenu           = document.getElementById('product-navigation-filter'), //actually menu to be trigged
                menuBackgroundColor  = document.querySelector('.product-menu');  

            menuLink.on('click', ProductMenu);

            function ProductMenu( event ) {

                event.preventDefault();
                event.stopPropagation();
                
                //for this --> function
                classie.toggle(this,'active'); //Show link is activate
                
                //toggling class
                classie.toggle(filterMenu, 'product-filter-open'); //menu is open
                
                classie.toggle(menuBackgroundColor, 'product-filter-background'); //background color change
                
                //function to disable other links
                disableOther(menuLink);

            }
           
            function disableOther( link ) {
                if( link !== menuLink) {
                  classie.toggle(menuLink, 'disabled');
                }
            }
        },
        ScrollToLogic:function() {
            

            
        }
    };
})(  jQuery, document, window, _ , undefined );



/*
 *
 * Calling functions
 *
 */

indieScrapInitilazer.ProductFilter();
indieScrapInitilazer.LeftGlobalSiteSearch();
indieScrapInitilazer.ProductMenuToggling();
indieScrapInitilazer.ScrollToLogic();

