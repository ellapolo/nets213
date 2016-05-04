var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/cis197hw5', function (err) {
  if (err && err.message === 'connect ECONNREFUSED') {
    console.log('Error connecting to mongodb database: %s.\nIs "mongod" running?', err.message);
    process.exit(0);
  } else if (err) {
    throw err;
  } else {
    console.log('DB successfully connected. Adding seed data...');
  }
});

var db = mongoose.connection;

var truckSchema = new mongoose.Schema({
  _id: Number,
  latitude: Number,
  longitude: Number,
  name: String,
  menu: [{item: String, price: Number}],
});

var updates = new mongoose.Schema({
  id: Number,
  name_update: [{name: String, votes: Number}],
  menu_update: [{item: String, price: Number, votes: Number}],
});

var Truck = mongoose.model('Truck', truckSchema);
var Update = mongoose.model('Update', updates);

module.exports = {
  Truck: Truck,
  Update: Update,
  mongoose: mongoose,
  db: db.collection('Truck')
}