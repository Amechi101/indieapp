
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

    return {

        GlobalMenus: function() {

            /*
             *
             * Toggle functionality for Product Menu
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

            var filterDropdown = new Dropdown($('#global-site-letter, #global-site-sex, #product-categories, #product-price-filter, #product-trending-filter'));

            /*
             *
             * Functionality for Left Global Menu & Website Search
             *
             */

            var globalHtml = $('html'),
                globalNav = $('.navigation'),
                globalSearch = $('.website-filtersearch'),
                globalOpenNav = $('#indie-global-menu a.btn-toggle-sidebar-left'),
                globalOpenWebSeach = $('#indie-global-menu a.btn-toggle-sidebar-right'),
                globalCloseNav = $('#indie-global-menu-close'),
                globalCloseWebSearch = $('#indie-global-websearch-close');


                //Menu
                globalOpenNav.on( 'click' , function( event ) {
            
                    //prevent page from going up top
                    event.preventDefault();
                    event.stopPropagation();
                
               
                    globalNav.addClass('is--active'); 
                    globalHtml.addClass('is--overflow');
                    
                });

                //Website filter
                globalOpenWebSeach.on( 'click' , function( event ) {
            
                    //prevent page from going up top
                    event.preventDefault();
                    event.stopPropagation();
                
               
                    globalSearch.addClass('is--active-search'); 
                    globalHtml.addClass('is--overflow');
                    
                });


                //menu close
                globalCloseNav.on( 'click' , function( event ) {
            
                    //prevent page from going up top
                    event.preventDefault();
                    event.stopPropagation();
            
                    
                    //toggling class with effects
                    globalNav.removeClass('is--active'); 
                    globalHtml.removeClass('is--overflow');
            
                });

                //Search close
                globalCloseWebSearch.on( 'click' , function( event ) {
            
                    //prevent page from going up top
                    event.preventDefault();
                    event.stopPropagation();
            
                    
                    //toggling class with effects
                    globalSearch.removeClass('is--active-search'); 
                    globalHtml.removeClass('is--overflow');
            
                });
        },
        JsPluginInitilaizers:function() {
            
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

            /*
             *
             * Plugin intializers
             *
             */

            $('.indie-home-section').flickerplate({
                auto_flick: false,
                // auto_flick_delay: 10,
                flick_animation: 'transform-slide',
                dot_navigation: false,
            });

            
        }
    };
})(  jQuery, document, window, _ , undefined );



/*
 *
 * Calling functions
 *
 */
indieScrapInitilazer.GlobalMenus();
indieScrapInitilazer.JsPluginInitilaizers();

