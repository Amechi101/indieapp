
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
     * Private Methods
     *
     */

    // http://coveroverflow.com/a/11381730/989439
    function mobilecheck() {
        var check = false;
        (function(a){if(/(android|ipad|playbook|silk|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4)))check = true})(navigator.userAgent||navigator.vendor||window.opera);
        return check;
    }


    /*
     *
     * Public API Methods
     *
     */
    return {

        GlobalJS: function() {

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
             * Scroll Up functionality
             *
             */
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
             * Functionality for Left Global Menu & Website Search & Product Detail
             *
             */

            var cardContainer = Array.prototype.slice.call( document.querySelectorAll( '.hover-container' ) ),
                eventType =  mobilecheck() ? 'touchstart' : 'click';

          
            cardContainer.forEach(function (element, index) {


                var cardTargetsOpen = element.querySelector( '.hover-container > a.card-view' ),
                    cardTargetsContainer = element.querySelector( '.hover-container > div.card-cover' ),
                    cardTargetsClose = element.querySelectorAll( '.hover-container > div.card-cover > a.card-close' );


                    console.log(cardTargetsContainer);

                            
                cardTargetsOpen.addEventListener(eventType, function( event ) {
                    event.preventDefault();
                    event.stopPropagation();


                    classie.add( cardTargetsContainer, 'card--active' );
                } ,false);

                Array.prototype.slice.call( cardTargetsClose ).forEach(function( closeTarget ) {

                    closeTarget.addEventListener(eventType, function( event ) {
                        event.preventDefault();
                        event.stopPropagation();


                        classie.remove( cardTargetsContainer, 'card--active' );
                    
                    } ,false);

                });
            });


            //@TODO revise the functionality, refactor code      
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
    };//return end
})(  jQuery, document, window, _ , undefined );



/*
 *
 * Calling functions
 *
 */
indieScrapInitilazer.GlobalJS();
indieScrapInitilazer.JsPluginInitilaizers();

