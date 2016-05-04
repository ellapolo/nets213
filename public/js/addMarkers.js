function initMap() {
	var mapDiv = document.getElementById('map');

	var map = new google.maps.Map(mapDiv, {
		center: {lat: 39.9502, lng: -75.1913},
		zoom: 17
	});


	setMarkers(map);
}

var trucks = []; 

//begin reading the global variable json containing information about the trucks and populate the trucks list
for (var i = 0; i < json.length; i++) {	
	var truck = [];
	truck.push(json[i]['name']);
	truck.push(parseFloat(json[i]['lat']));
	truck.push(parseFloat(json[i]['long']));
	var menu = JSON.parse(json[i]['menu']);
	var food = '';
	for (var items in menu) {
		food += '<p> ' + items + ' - ' + '$' + menu[items] + '</p>';
	}
	truck.push(food);
	trucks.push(truck);
}

function setMarkers(map) {
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
				'<div id="bodyContent">'+ truck[3]
			});
			marker.addListener('click', function() {
				infowindow.open(map, marker);
			});
		})(i);
	}
}