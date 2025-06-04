from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2018_simple.csv')
lines =path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#extract dates and high temperatures.
dates, highs = [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
    except (ValueError, IndexError):
        # Skip rows with missing or malformed data
        continue
    dates.append(current_date)
    highs.append(high)

#plot the high temperatures.

fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

#format plot
ax.set_title('Daily High Temperatures, 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()#draws the date labels diagonally to prevent them from overlapping
ax.set_ylabel('Temperature(F)', fontsize=16)
ax.tick_params(labelsize=16)

# plt.savefig('sitka_highs.png', bbox_inches='tight')
plt.show()
