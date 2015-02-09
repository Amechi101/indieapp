"use strict";

/*
 *
 * List of all websites
 *
 */

var websiteSearchCollection = Backbone.Collection.extend({});
var websitesCollection = new websiteSearchCollection({model:websites});

websitesCollection.reset(websites);



