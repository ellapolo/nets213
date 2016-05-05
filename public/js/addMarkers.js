function initMap() {
	var mapDiv = document.getElementById('map');

	var map = new google.maps.Map(mapDiv, {
		center: {lat: 39.9502, lng: -75.1913},
		zoom: 17
	});


	setMarkers(map);
}

//begin reading the global variable json containing information about the trucks and populate the trucks list
function parseTruckData(truck_json) {
	var trucks = []
	for (var i = 0; i < truck_json.length; i++) {	
		var truck = [];
		truck.push(truck_json[i]['name']);
		truck.push(parseFloat(truck_json[i]['lat']));
		truck.push(parseFloat(truck_json[i]['long']));
		var menu = JSON.parse(truck_json[i]['menu']);
		var food = '';
		for (var items in menu) {
			food += '<p> ' + items + ' - ' + '$' + menu[items] + '</p>';
			}
		truck.push(food);
		trucks.push(truck);
	}
	return trucks;
}

function sendUpdate() {
	alert("hello!");
	console.log("I'm alive!")
}

function setMarkers(map) {
	trucks = parseTruckData(trucks_json);
	console.log(trucks)
	var image = {
		url: 'https://dl.dropboxusercontent.com/u/76571929/truckLogo.png'
	};

	var listeners = [];
	for (var i = 0; i < trucks.length; i++) {
		(function(index){
			var truck = trucks[index];
			var marker = new google.maps.Marker({
				position: {lat: truck[1], lng: truck[2]},
				map: map,
				icon: image,
				title: truck[0]
			});
			var infowindow = new google.maps.InfoWindow({
				content: '<div id="content">'+
				'<div id="siteNotice">'+
				'</div>'+
				'<h1 id="firstHeading" class="firstHeading">' + truck[0] + '</h1>' +
				'<input type="text" name="xentry" id="xentry" class="search form-control" value="" autocomplete="off" placeholder="Item - $(price)"/>' + 
				'<button id="add_entry" onClick = "sendUpdate()" type="button">Add to Database</button>' +
				'<div id="result"></div>' +
				'<div id="bodyContent">'+ truck[3]
			});
			marker.addListener('click', function() {
				infowindow.open(map, marker);
			});
		})(i);
	}
}