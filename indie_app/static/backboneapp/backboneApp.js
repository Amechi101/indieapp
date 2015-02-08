// // @TODO To design with the tastypie api to filter and generate dropdown search list (with cancelable componenets) and search filter for the entire site with 
// // all functionality attached in this JS file. For: Collection. Views. and Model.


// /*
//  *
//  * Backbone Model ( returing URL from tastypie link and craeting the list defaults for the dropdown on the search page)
//  *
//  */
// var productFliter = Backbone.Model.extend({
//     defaults :{
//         // @TODO update logic to backend to change as to what site is currently being choosen by the user on the front-end
//         categories:[],
//         priceRange:['0-50', '50-100','100-200','200-300','400+'],
//         generalFilter:['Newest Scrape\'s','Oldest Scrape\'s','Popular Scarpe\'s']
//     }
// });

// /*
//  *
//  * Backbone Collection (To expose the API link for consumpation)
//  *
//  */
// var productCollection = Backbone.Collection.extend({
    
//     model:productFliter,
//     url:'http://127.0.0.1:8000/scrap_api/_internal_productall_api/v2/all_wesbsites/'

// });


// var productView = Backbone.View.extend({
//     //this is the scope of the Backbone selector, choosing the descendants of the
//     el:'.wrapper-nav',

//     initialize: function() {
//         _.bindAll(this,'render','filterFunc');
      
//         this.render();
//     },
//     filterFunc: function() {
//         //Array to access the information from the backbone models
//         var productFilterItems = [this.model.attributes.categories, this.model.attributes.priceRange, this.model.attributes.generalFilter];
     
//           /*
//             Looping construct to add the elements from the model in a <li> tag this will allow for easier access to attach any events and data 
//             that needs to be transferred to the backend.

//           */
//         for (var i = 0, j=0, k=0; i < productFilterItems[0].length || j < productFilterItems[1].length || k < productFilterItems[2].length; i++, j++, k++) {
        

//             //categories filter
//             if ( i < productFilterItems[0].length ) {
//               $('#categories', this.el).append('<li>' + productFilterItems[0][i] + '</li>');  
//             }

//             //price filter
//             if ( k < productFilterItems[1].length ) {
//               $('#price', this.el).append('<li>$' + productFilterItems[1][i].replace('-', '-$') + '</li>');
//             }
            
//             //trending filter
//             if ( j < productFilterItems[2].length ) {
//               $('#categories', this.el).append('<li>' + productFilterItems[2][i] + '</li>');  
//             }
            
//         }
      
//     },
//     render: function() {
//         this.filterFunc();
//     }
// });

// //Model
// var productFliterObject  = new productFliter();

// //Collection
// var productCollectionObject = new productCollection();

// // View Dropdown
// var productViewObject = new productView({model:productFliterObject});

// // console.log(productFliterObject)
// // console.log(productViewObject)



// @TODO To design with the tastypie api to filter and generate dropdown search list (with cancelable componenets) and search filter for the entire site with 
// all functionality attached in this JS file. For: Collection. Views. and Model.




