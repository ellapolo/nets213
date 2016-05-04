var mongo = require ('./mongo');
var uuid = require('node-uuid');


module.exports = {
  createTruck: function (tid, tname, tlatitude, tlongitude, tmenu, callback) {
    var truck = new mongo.Truck({_id: tid, latitude: tlatitude, longitude: tlongitude, menu:tmenu});
    truck.save(function (error) {
      callback(error, tid);
    });
  },

  getAllTrucks: function (callback) {
    mongo.Truck.find(function (error, products) {
      callback(error, products);
    });
  },

  getTruck: function (_id, callback) {
    mongo.Truck.findById(_id, function (error, product) {
      callback(error, product);
    });
  },

};
