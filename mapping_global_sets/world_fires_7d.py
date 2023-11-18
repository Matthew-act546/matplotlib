import csv

from plotly.graph_objs import scattergeo, Layout
from plotly import offline

filename = 'mapping_global_sets/data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next_row = next(reader)

    # for index, row in enumerate(next_row):
    #     print(index, row)

    lons, lats, dates, times, daynights, brights = [], [], [], [], [], []
    for row in reader:
        try:
            lon = float(row[1])
            lat = float(row[0])
            date = str(row[5])
            time = str(row[6])
            daynight = str(row[12])
            bright = float(row[2])
        except IndexError:
            print(f" {row} error")
        else:
            lons.append(lon)
            lats.append(lat)
            dates.append(date)
            times.append(time)
            daynights.append(daynight)
            brights.append(bright)

adj_bright = [bright/40 for bright in brights]
adj_date = [f"DATE: {date}" for date in dates]
adj_time = [f"TIME: {time[:2]}:{time[2:4]}" for time in times]
adj_day = [f"DAY/NIGHT: {day}" for day in daynights]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': adj_date,
    'marker': {
        'size': adj_bright,
        'color': adj_bright,
        'colorscale': 'jet',
        'reversescale': False,
        'colorbar': {'title':'Brightness'},
    },
}]

my_layout = Layout(title="World Fires in 7days")
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="mapping_global_sets/world_fires_7d.html")