from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#extract high temperatures.
highs = []
for row in reader:
    try:
        high = int(row[5])
    except ValueError:
        continue
    highs.append(high)

print(highs)







