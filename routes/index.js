var trucksDb = require("../db/truck")


exports.init = function(callback) {
	callback();
};

exports.index = function(req, res) {
	res.render('landing');

}