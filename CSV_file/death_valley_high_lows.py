import matplotlib.pyplot as plt
from datetime import datetime

import csv

filename = 'CSV_file/data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, lows, highs = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing date: {current_date}")
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)    

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
title = "Daily High and low temperatures 2018\nDeath Valley, CA"
plt.title(title , fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which="major", labelsize=16)

plt.show()             