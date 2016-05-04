var trucksDb = require("../db/truck")
var truckData = require("../data/external_menus.json")

exports.init = function(callback) {
	callback();
};

exports.index = function(req, res) {

	res.render('landing.ejs', {trucks: truckData});

}

exports.update = function(req, res) {

}