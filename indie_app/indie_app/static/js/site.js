/*

	*--------------------------------------------------------------------*
	
	Indie-Scrap interface design 

	Copyright (C) 2014 Indie-Scrap 
	
	*--------------------------------------------------------------------*

*/

var Initilazer = (function( $ , _ ) {
	/*
		**Imported mixins** 
		- Jquery
		- underscore
	*/

	//Private variables
	var _window = $(window),
	      _body = $('body');
	



	return {
		// backBoneApplication: function() {
		// 	var userRegistration = Backbone.View.extend({
		// 		el: $('div.load-form'),
		// 		events: {
		// 			'click a#login': 'addLoginPage'
		// 		},
		// 		template: _.template( $('#signUpTemplate').html() ),
		// 		initialize: function() {
		// 			_.bindAll(this, 'addLoginPage');
		// 		},
		// 		addLoginPage: function() {
		// 			this.$el.html(this.template());
		// 		}
		// 	});
			
		// 	var userRegistration = new userRegistration();
		// },
		// scrollMenu: function() {
		// 	var _headerMenu = $('#header-menu'),
		// 		_productMenu = $('#product-menu');

		// 	_window.scroll(function() {
		// 		var _this = $(this); // this --> window

		// 		if ( _this.scrollTop() > ( _headerMenu.height() ) ) {
		// 			_productMenu.filter(function ( index ) {
		// 	    		return index === 0;
		// 	  		}).css({ position:'fixed', top:0});

		// 	  		_headerMenu.css({display:'none'});
		// 		} else {
		// 			_productMenu.filter(function ( index ) {
		// 	    		return index === 0;
		// 	  		}).css({ position:'relative'}); 

		// 	  		_headerMenu.css({display:'inline-block'});
		// 		}
		// 	});
  //   	}	
	};
	

})( jQuery, _ );


//Calling functions
// Initilazer.backBoneApplication();
Initilazer.scrollMenu();











	


	



    // EventCore.prototype = {

    // 	$element: null,
    	

    // 	init: function( element ) {


    // 		this.$element = $(element);

    // 		console.log(this.$element)
    // 	}
    // };

    // EventCore();




	// win.scroll( function () {
		
	// 	$element = $(this);

	// 	 console.log($element);


	// 	if ( $element.scrollTop() > 1) {

			
	// 		$('#header').addClass('stuck');

	// 	} else {
	// 		$('#header').removeClass('stuck');
	// 	}

     
	// });


	// var navigation = $('#header');
	// var elemTop = parseInt(navigation.offset().top, 10);
	// var elemBottom = elemTop + navigation.height()


	// navigation.scroll(function()  {
	// 	if( elemTop >= elemBottom ) {
	// 	console.log('down, now add new header');
	// }
	// });
	





	// var docViewTop = $(window).scrollTop(),
 //                docViewBottom = docViewTop + $(window).height(),
 //                elemTop = parseInt($element.offset().top, 10),
 //                elemBottom = elemTop + $element.height();

 //            if ( 
 //                //bottom of element is lower than the top of the page
 //                (elemBottom + this.settings.buffer >= docViewTop ) && 
 //                //top of the element is higher than the bottom of the page
 //                (elemTop <= docViewBottom + this.settings.buffer) && 

 //                //bottom of the element is higher than bottom of the document
 //                (elemBottom <= docViewBottom + this.settings.buffer) && 

 //                //top of the element is lower than top of the document
 //                (elemTop + this.settings.buffer >= docViewTop) ) 
 //            {
 //                return true;
 //            } else {
 //                return false;
 //            }


