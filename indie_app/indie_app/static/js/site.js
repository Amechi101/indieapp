/*

*--------------------------------------------------------------------*

Indie-Scrap interface design 

Copyright (C) 2014 Indie-Scrap 

*--------------------------------------------------------------------*

*/

"use strict";

//To avoid namespace collision
var indieScrapInitilazer =  indieScrapInitilazer || {};

indieScrapInitilazer = (function ( $, document, window, _ ,  undefined ) {


	return {
		BackboneApp: function() {
			
			var productFliter = Backbone.Model.extend({
				defaults :{
					categories:{
                        // @TODO update logic to backend to change as to what site is currently being choosen by the user on the front-end
                        // for men and women
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
		MenuToggling:function() {
			
			
			/*
             *
             * Product filtering
             *
             */
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

			
            /*
             *
             * Dashboard navigation for user accounts
             *
             */
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
	
		}
	};
})( jQuery, document, window, _ ,  undefined);




/*
 *
 * Calling functions
 *
 */

indieScrapInitilazer.BackboneApp();
indieScrapInitilazer.MenuToggling();










