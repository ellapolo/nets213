var express = require('express');
var app = express();
var path = require('path');
var routes = require('./routes')

app.set('port', (process.env.PORT || 5000));


// Serve static pages
app.engine('html', require('ejs').__express);
app.set('view engine', 'html');
app.use(express.static(__dirname + '/public'));


routes.init(function() {
	app.get('/', routes.index);
	app.post('/update_menu', routes.update_menu);

	app.listen(app.get('port'), function() {
  		console.log('Node app is running on port', app.get('port'));
	});	
});


// Start listening for requests
