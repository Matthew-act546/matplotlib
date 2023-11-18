import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename= 'mapping_global_sets/data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next_row = next(reader)

    for index, row in enumerate(next_row):
        print(index, row)

    lons, lats, brights, times,  =[], [], [], []
    for row in reader:
        lon = float(row[1])
        lat = float(row[0])
        bright = float(row[2])
        time = str(row[6])

        lons.append(lon)
        lats.append(lat)
        brights.append(bright)
        times.append(time)

time_config = [f"occur on {time[:2]}:{time[2:4]}" for time in times]
adj_bright = [bright/40 for bright in brights]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': time_config,
    'marker': {
        'size': adj_bright,
        'color': adj_bright,
        'colorscale': 'jet',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'}
    },
}]

my_layout = Layout(title="World Fires in Day 1")
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='mapping_global_sets/world_fires.html')

