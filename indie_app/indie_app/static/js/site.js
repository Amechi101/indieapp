
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
    /*
     *
     * Private functions
     *
     */

    // Write them below


    return {

        GlobalSiteFilter: function() {

            /*
             *
             * Toggle functionality
             *
             */
            function Dropdown( element ) {
                    
                this.el = element;
                this.initEvents(); 
                
            }

            Dropdown.prototype = {
                initEvents:function() {
                    this.el.on('click', function( event ) {
                        event.stopPropagation();
                        $(this).toggleClass('active');
                    });
                }
            };

            var filterDropdown = new Dropdown($('#global-site-letter, #global-site-trending, #global-site-sex, #price-filter, #trending-product-filter'));
   
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
            
            var $elScroll = $('#scrollTop');

            $(window).scroll(function() {
                if( $(this).scrollTop() > 100 ) {
                    $elScroll.fadeIn();
                } else {
                    $elScroll.fadeOut();
                }
            });

            $elScroll.on('click', function() {
                $('html, body').animate({
                    scrollTop:0
                }, 600);

                return false;
            });
     
        }
    };
})(  jQuery, document, window, _ , undefined );



/*
 *
 * Calling functions
 *
 */
indieScrapInitilazer.GlobalSiteFilter();
indieScrapInitilazer.ScrollToLogic();

