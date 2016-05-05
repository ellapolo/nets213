var trucksDb = require("../db/truck")
var updateDb = require("../db/update")
var truckData = require("../data/external_menus.json")

exports.init = function(callback) {                                                
	callback();
};

exports.index = function(req, res) {
	res.render('landing.ejs');

}

exports.update_menu = function(req, res) {
	console.log(req);
	updateText = req.body.update;
	id = req.body.id;
	var data = updateText.split('-');
	if (data.length < 2) {
		console.log("invalid update sent.");
		res.send("something");
	}
	var item = data[0];
	var price = data[1];
	update = {_id: id, name_update: null, item_update: {item: item, price: price}}
	updateDb.addUpdate(id, update, function(err) {
		if (err) {
			console.log(err);
		} else {
			console.log("successfully added update for menu of truck " + id);
		}
	});

}

function saveTrucks(callback) {
	for (var i = 0; i < truckData.length; i++) {	
		console.log("adding truck " + i + " to the database");
		var id = truckData[i]['id'];
		var name = truckData[i]['name'];
		var latitude = truckData[i]['lat'];
		var longitutde = truckData[i]['long'];
		var menu = truckData[i]['menu'];
		trucksDb.createTruck(i+1, name, latitude, longitutde, menu, function(err) {
			if (err) {
				console.log(err);
			} else {
				console.log("successfully added truck " + i + "to the database!");
			}
		});
	}		
}	