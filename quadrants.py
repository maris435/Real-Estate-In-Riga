import folium
import math

# Define the boundaries of Riga in terms of latitude and longitude
min_lat = 56.880525
max_lat = 57.073682
min_lon = 23.942295
max_lon = 24.255976

# Calculate the number of quadrants in each direction
num_quadrants_lat = math.ceil((max_lat - min_lat) / 0.005)
num_quadrants_lon = math.ceil((max_lon - min_lon) / 0.005)

# Create a map centered on Riga
map_riga = folium.Map(location=[(min_lat + max_lat) / 2, (min_lon + max_lon) / 2], zoom_start=11)

# Iterate over the latitude and longitude ranges
for lat in range(num_quadrants_lat):
    for lon in range(num_quadrants_lon):
        # Calculate the boundaries of the current quadrant
        quadrant_min_lat = min_lat + lat * 0.005
        quadrant_max_lat = quadrant_min_lat + 0.005
        quadrant_min_lon = min_lon + lon * 0.005
        quadrant_max_lon = quadrant_min_lon + 0.005

        # Create a rectangle marker for the quadrant
        folium.Rectangle(
            bounds=[(quadrant_min_lat, quadrant_min_lon), (quadrant_max_lat, quadrant_max_lon)],
            fill=True,
            fill_color='red',
            fill_opacity=0.4
        ).add_to(map_riga)

# Save the map as an HTML file
map_riga.save('riga_map.html')
