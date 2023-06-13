import folium
from preprocessing import extract_data
import math

df = extract_data()

min_lat = 56.880525
max_lat = 57.073682
min_lon = 23.942295
max_lon = 24.255976



# Create a map centered on Riga
map_object = folium.Map(location=[(min_lat + max_lat) / 2, (min_lon + max_lon) / 2], zoom_start=11)

for index, row in df.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']
    marker = folium.Marker(location=[latitude, longitude])
    marker.add_to(map_object)

map_object.save('waypoint_map.html')
