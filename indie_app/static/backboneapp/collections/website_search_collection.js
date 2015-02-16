"use strict";

/*
 *
 * List of all websites
 *
 */
for(var i = 0; i < websites.length; i++) {
	var pk = websites[i].pk;
	websites[i] = websites[i].fields;
	websites[i].pk = pk;
}

var websiteSearchCollection = Backbone.Collection.extend({});
var websitesCollection = new websiteSearchCollection({model:websites});

websitesCollection.reset(websites);



