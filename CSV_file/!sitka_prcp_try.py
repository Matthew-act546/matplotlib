import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'CSV_file/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high temperatures from this profile
    dates, lows, highs, prcps = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        prcp = float(row[3])
        dates.append(current_date)
        prcps.append(prcp)
        lows.append(low)
        highs.append(high)

# plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, prcps, c='green')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
plt.title("Daily High and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which="major", labelsize=16)

plt.show()