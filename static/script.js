document.addEventListener('DOMContentLoaded', function() { 
    // Initialize the map on the "mapid" div with a given center and zoom
    var mymap = L.map('mapid').setView([-74.083, 4.5921], 2); // You can adjust the initial view

    // Load and display tile layers on the map (default OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18,
    }).addTo(mymap);

    // Function to handle map clicks
    function onMapClick(e) {
        var lat = e.latlng.lat;
        var lng = e.latlng.lng;

        // Display a marker where the user clicked on the map (optional)
        var marker = L.marker([lat, lng]).addTo(mymap);
        marker.bindPopup("<b>Location Selected</b><br>Latitude: " + lat + "<br>Longitude: " + lng).openPopup();

        // Here, you might want to send the latitude and longitude to your Flask backend
        fetch('/get_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                lat: lat,
                lon: lng,
            }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            // Process and display the data received from Flask (e.g., update UI or show another popup)
            marker.setPopupContent("<b>Location Selected</b><br>Latitude: " + lat + "<br>Longitude: " + lng + "<br>Radiation: " + data.radiation).openPopup();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    // Attach the click event handler to the map
    mymap.on('click', onMapClick);
});
