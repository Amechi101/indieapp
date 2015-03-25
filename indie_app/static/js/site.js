/**
 * Unlabel App v1.0.0
 * 
 *
 * author: Unlabel Team
 * 
 * 
 * Copyright 2015, Unlabel
 * http://www.unlabel.us
 */

"use strict";


//To avoid namespace collision
var UnlabelInitilazer =  UnlabelInitilazer || {};

UnlabelInitilazer = (function ( $, document, window, undefined  ) {

    /* --------------------------------------------
     Platform detect
     --------------------------------------------- */
    var mobileTest;
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
        mobileTest = true;
        $("html").addClass("mobile");
    }
    else {
        mobileTest = false;
        $("html").addClass("no-mobile");
    }
    
    var mozillaTest;
    if (/mozilla/.test(navigator.userAgent)) {
        mozillaTest = true;
    }
    else {
        mozillaTest = false;
    }
    var safariTest;
    if (/safari/.test(navigator.userAgent)) {
        safariTest = true;
    }
    else {
        safariTest = false;
    }
    
    // Detect touch devices    
    if (!("ontouchstart" in document.documentElement)) {
        document.documentElement.className += " no-touch";
    }
    
    
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

            

            // var hashMenuClosing = $('.navigation > .navigation__primary > ul > li > a');

            // console.log(hashMenuClosing)

            // if( hashMenuClosing ) {
            //     // Hash menu forwarding
            //     if (window.location.hash === "#brands"){
            //         var hash_offset = $(window.location.hash).offset().top;
            //         $("html, body").animate({
            //             scrollTop: hash_offset
            //         });
            //     }
            // }
            
        }
    };//return end
})(  jQuery, document, window, undefined );



/*
 *
 * Calling functions
 *
 */
UnlabelInitilazer.GlobalJS();


