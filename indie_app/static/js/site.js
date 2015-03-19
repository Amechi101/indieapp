
/*

*--------------------------------------------------------------------*

Indie-Scrap interface design 

Copyright (C) 2014 Indie-Scrap 

*--------------------------------------------------------------------*

*/

"use strict";

//To avoid namespace collision
var indieScrapInitilazer =  indieScrapInitilazer || {};

indieScrapInitilazer = (function ( $, document, window, undefined  ) {
    
    return {
        GlobalJS: function() {

            /*
             *
             * Toggle functionality for Brand Search
             *
             */
            function Dropdown( element ) {
                    
                this.el = element;
                this.initEvents(); 
                
            }

            Dropdown.prototype = {
                initEvents:function() {
                    this.el.on( 'click' , function( event ) {
                        event.stopPropagation();
                        $(this).toggleClass('active');
                    });
                }
            };

            var filterDropdown = new Dropdown($('#global-site-sex'));

            
            /*
             *
             * Page Transitions
             *
             */
           
            $(".animsition").animsition({
  
                inClass               :   'fade-in-left',
                outClass              :   'fade-out-left',
                inDuration            :    1500,
                outDuration           :    800,
                linkElement           :   '.animsition-link',
                // e.g. linkElement   :   'a:not([target="_blank"]):not([href^=#])'
                loading               :    true,
                loadingParentElement  :   'body', //animsition wrapper element
                loadingClass          :   'animsition-loading',
                unSupportCss          : [ 'animation-duration',
                                          '-webkit-animation-duration',
                                          '-o-animation-duration'
                                        ],
                //"unSupportCss" option allows you to disable the "animsition" in case the css property in the array is not supported by your browser.
                //The default setting is to disable the "animsition" in a browser that does not support "animation-duration".
                
                overlay               :   false,
                
                overlayClass          :   'animsition-overlay-slide',
                overlayParentElement  :   'body'
            });

            
            /*
             *
             * Global Menu
             *
             */
           
            var globalHtml = $('html'),
                globalNav = $('.navigation'),
                globalOpenNav = $('#indie-global-menu-open'),
                globalCloseNav = $('#indie-global-menu-close');


            //Menu Open
            globalOpenNav.on( 'click' , function( event ) {
        
                //prevent page from going up top
                event.preventDefault();
                event.stopPropagation();
            
                globalNav.addClass('is--active'); 
                globalHtml.addClass('is--overflow'); 
            });

            //menu close
            globalCloseNav.on( 'click', function( event ) {
        
                //prevent page from going up top
                event.preventDefault();
                event.stopPropagation();
                
                //toggling class with effects
                globalNav.removeClass('is--active'); 
                globalHtml.removeClass('is--overflow');
        
            });
        }
    };//return end
})(  jQuery, document, window, undefined );



/*
 *
 * Calling functions
 *
 */
indieScrapInitilazer.GlobalJS();


