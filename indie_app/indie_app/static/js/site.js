/*

*--------------------------------------------------------------------*

Indie-Scrap interface design 

Copyright (C) 2014 Indie-Scrap 

*--------------------------------------------------------------------*

*/

"use strict";

//To avoid namespace collision
var indieScrapInitilazer =  indieScrapInitilazer || {};

indieScrapInitilazer = (function( $, document, window, _ ,  undefined ) {


	//Private variables
	var _window = document.window,
		_body   = document.body;

	return {
		BackboneApp: function() {
			
			var productFliter = Backbone.Model.extend({
				defaults :{
					categories:{
						men:['Tops','Bottoms','Shorts','Jackets & Blazers','Sweaters','Outerwear','Shoes','Accessories','Undergarments'],
						women:['Dresses','Tops','Skirts','Shorts','Bottoms','Jumpsuits & Rompers','Jackets & Blazers','Sweaters','Outerwear','Shoes','Accessories','Lingerie']
					},
					priceRange:['0-50', '50-100','100-200','200-300','400+'],
					generalFilter:['Newest Scrap\'s','Oldest Scrap\'s','Popular Scarp\'s']
				}

			});

			var productView = Backbone.View.extend({
				//this is the scope of the Backbone selector, choosing the descendants of the
				el:'#product-navigation .filter-options',

				initialize: function() {
					_.bindAll(this,'render','filterFunc');
					
					this.render();
				},
				filterFunc: function() {
					//Array to access the information from the backbone models
					var productFilterItems = [this.model.attributes.categories.men, this.model.attributes.categories.women, this.model.attributes.priceRange, this.model.attributes.generalFilter];
					var menuFilter = $('#men', this.el);
					
					/*
						Looping construct to add the elements from the model in a <li> tag this will allow for easier access to attach any events and data that needs to 
						be transferred to the backend.

					*/
					for (var i = 0, j=0, k=0, l=0; i < productFilterItems[0].length || j < productFilterItems[1].length || k < productFilterItems[2].length || l < productFilterItems[3].length ; i++, j++, k++, l++) {
						
						//mens filter
						if ( i < productFilterItems[0].length ) {
							$('#men', this.el).append('<li id="' + productFilterItems[0][i] + '" class="product-options"><span></span>' + productFilterItems[0][i] + '</li>');	
						}

						//womens filter
						if ( j < productFilterItems[1].length ) {
							$('#women', this.el).append('<li id="' + productFilterItems[1][i] + '" class="product-options"><span></span>' + productFilterItems[1][i] + '</li>');
						}
						
						//price filter
						if ( k < productFilterItems[2].length ) {
							$('#price', this.el).append('<li id="' + productFilterItems[2][i].replace('+','') + '" class="product-options"><span></span>$' + productFilterItems[2][i].replace('-', '-$') + '</li>');
						}

						// filter
						if ( l < productFilterItems[3].length ) {
							$('#other', this.el).append('<li id="' + productFilterItems[3][i].replace('+','') + '" class="product-options"><span></span>' + productFilterItems[3][i] + '</li>');
						}
					}
					
				},
				render: function() {
					this.filterFunc();
				}
			});
			
			var productFliterObject  = new productFliter();
			var productViewObject = new productView({model:productFliterObject});

			// console.log(productFliterObject)
			// console.log(productViewObject)

		}, 
		MenuToggleFunc:function() {
			/*
				For Responsive and Product Navigation site wide
			*/
			
			//Product Navigation
			var menuLink             = $('#menu-toggle'), //trigger for menu
				filterMenu           = $('#product-navigation-filter'), //actually menu to be trigged
				menuBackgroundColor  = $('.product-menu');	

			menuLink.on('click', function( event ) {
				
				//prevent page from going up top
				event.preventDefault();
				
				//for this --> function
				classie.toggle(this,'active'); //Show link is activate
				
				//toggling class
				filterMenu.toggleClass('product-filter-open'); //menu is open
				menuBackgroundColor.toggleClass('product-filter-background'); //background color change
				
				//function to disable other links
				disableOther(menuLink);
			});
			
			function disableOther( link ) {
				if( link !== menuLink) {
					classie.toggle(menuLink, 'disabled');
				};
			}

			//Dashboard navigation
			$('#nav-accordion').dcAccordion({
		        eventType: 'click',
		        autoClose: true,
		        saveState: true,
		        disableLink: true,
		        speed: 'slow',
		        showCount: false,
		        autoExpand: true,
		        // cookie: 'dcjq-accordion-1',
		        classExpand: 'dcjq-current-parent'
    		});

			//Responsive mobile Navigation
	
		}
	};
})( jQuery, document, window, _ ,  undefined);


//Calling functions
indieScrapInitilazer.BackboneApp();
indieScrapInitilazer.MenuToggleFunc();



/*!
 *
 *  Copyright (c) David Bushell | http://dbushell.com/
 *
 */
;(function (window, document, undefined) {

    // helper functions

    var trim = function(str)
    {
        return str.trim ? str.trim() : str.replace(/^\s+|\s+$/g,'');
    };

    var hasClass = function(el, cn)
    {
        return (' ' + el.className + ' ').indexOf(' ' + cn + ' ') !== -1;
    };

    var addClass = function(el, cn)
    {
        if (!hasClass(el, cn)) {
            el.className = (el.className === '') ? cn : el.className + ' ' + cn;
        }
    };

    var removeClass = function(el, cn)
    {
        el.className = trim((' ' + el.className + ' ').replace(' ' + cn + ' ', ' '));
    };

    var hasParent = function(el, id)
    {
        if (el) {
            do {
                if (el.id === id) {
                    return true;
                }
                if (el.nodeType === 9) {
                    break;
                }
            }
            while((el = el.parentNode));
        }
        return false;
    };

    // normalize vendor prefixes

    var doc = document.documentElement;

    var transform_prop = window.Modernizr.prefixed('transform'),
        transition_prop = window.Modernizr.prefixed('transition'),
        transition_end = (function() {
            var props = {
                'WebkitTransition' : 'webkitTransitionEnd',
                'MozTransition'    : 'transitionend',
                'OTransition'      : 'oTransitionEnd otransitionend',
                'msTransition'     : 'MSTransitionEnd',
                'transition'       : 'transitionend'
            };
            return props.hasOwnProperty(transition_prop) ? props[transition_prop] : false;
        })();

    window.App = (function()
    {

        var _init = false, app = { };

        var inner = document.getElementById('inner-wrap'),

            nav_open = false,

            nav_class = 'js-nav';


        app.init = function()
        {
            if (_init) {
                return;
            }
            _init = true;

            var closeNavEnd = function(e)
            {
                if (e && e.target === inner) {
                    document.removeEventListener(transition_end, closeNavEnd, false);
                }
                nav_open = false;
            };

            app.closeNav =function()
            {
                if (nav_open) {
                    // close navigation after transition or immediately
                    var duration = (transition_end && transition_prop) ? parseFloat(window.getComputedStyle(inner, '')[transition_prop + 'Duration']) : 0;
                    if (duration > 0) {
                        document.addEventListener(transition_end, closeNavEnd, false);
                    } else {
                        closeNavEnd(null);
                    }
                }
                removeClass(doc, nav_class);
            };

            app.openNav = function()
            {
                if (nav_open) {
                    return;
                }
                addClass(doc, nav_class);
                nav_open = true;
            };

            app.toggleNav = function(e)
            {
                if (nav_open && hasClass(doc, nav_class)) {
                    app.closeNav();
                } else {
                    app.openNav();
                }
                if (e) {
                    e.preventDefault();
                }
            };

            // open nav with main "nav" button
            document.getElementById('nav-open-btn').addEventListener('click', app.toggleNav, false);

            // close nav with main "close" button
            document.getElementById('nav-close-btn').addEventListener('click', app.toggleNav, false);

            // close nav by touching the partial off-screen content
            document.addEventListener('click', function(e)
            {
                if (nav_open && !hasParent(e.target, 'nav')) {
                    e.preventDefault();
                    app.closeNav();
                }
            },
            true);

            addClass(doc, 'js-ready');

        };

        return app;

    })();

    if (window.addEventListener) {
        window.addEventListener('DOMContentLoaded', window.App.init, false);
    }

})(window, window.document);







