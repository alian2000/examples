import folium
import json
import time

center = [33.52281717966467,36.320036879375806
          ]
zoom=(16)
political_countries_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
)
alquds = folium.Map(center, zoom_start=zoom)
folium.GeoJson(political_countries_url).add_to(alquds)

folium.Marker(center, popup='Dome Of the Rock').add_to(alquds)
folium.CircleMarker(location=(32.7779,33.235),radius=250, fill_color='red').add_to(alquds)

alquds
    
    
