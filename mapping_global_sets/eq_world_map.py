import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename='mapping_global_sets/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    hover_title = eq_dict['properties']['title']

    lats.append(lat)
    lons.append(lon)
    mags.append(mag)
    hover_texts.append(hover_title)

# map the earthquakes. 
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Jet',
        'reversescale': False,
        
        'colorbar': {
            'title': 'Magnitude'
        },
    },
}]
my_layout = Layout(title="Global Earthquakes")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='mapping_global_sets/global_earthquakes.html')