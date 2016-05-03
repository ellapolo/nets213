function initMap() {
		var mapDiv = document.getElementById('map');

		var map = new google.maps.Map(mapDiv, {
			center: {lat: 39.9502, lng: -75.1913},
			zoom: 17
		});


		setMarkers(map);
	}

	var trucks = [
	['Tyson Bees', 39.9502, -75.1913,
	'<p>Korean BBQ SHort Rib Tacos - $3</p>'+
	'<p>Thai Basil Chicken Tacos - $3</p>'+
	'<p>Edamame Tacos - $3</p>'+
	'<p>Korean Beef Short Rib and Kimchi Burrito - $5</p>'+
	'<p>Grilled BBQ Lemongrass Pork Bahn Mi Sandwhich- $5</p>'+
	'<p>Steamed Pork Buns - $3</p>'+
	'<p>Curry of the Week over Rice - $6</p>'+
	'<p>Thai Basil Chicken over Rice- $6</p>'+
	'</div>'+
	'</div>'],
	['Kings Wok', 39.9503, -75.1914, 
	'<p>Choose the items below with meats (chicken, pork, beef, shrimp, tofu)</p>'+
	'<p>Lo Mein - $4.50</p>'+
	'<p>Fried Rice - $4.50</p>'+
	'<p>Chow Fun - $4.50</p>'+
	'<p>Egg Foo Young - $4.50</p>'+
	'</div>'+
	'</div>']
	];

	alert(trucks);



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