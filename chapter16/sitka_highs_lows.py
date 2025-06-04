from pathlib import Path                # Import Path for handling file paths
import csv                              # Import csv module for reading CSV files
from datetime import datetime           # Import datetime for parsing date strings

import matplotlib.pyplot as plt         # Import matplotlib for plotting

path = Path('weather_data/sitka_weather_2018_simple.csv')  # Set the path to the CSV file
lines = path.read_text().splitlines()   # Read the file and split it into lines

reader = csv.reader(lines)              # Create a CSV reader object
header_row = next(reader)               # Read the header row

# extract dates and high/low temperatures.
dates, highs, lows = [], [], []         # Initialize lists for dates, highs, and lows
for row in reader:                      # Loop through each row in the CSV
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Parse the date
        high = int(row[5])              # Convert the high temperature to int
        low = int(row[6])               # Convert the low temperature to int
    except (ValueError, IndexError):    # Handle missing or malformed data
        # Skip rows with missing or malformed data
        continue
    dates.append(current_date)          # Add the date to the list
    highs.append(high)                  # Add the high temp to the list
    lows.append(low)                    # Add the low temp to the list

# plot the high and low temperatures.

fig, ax = plt.subplots()                # Create a figure and axes for plotting
ax.plot(dates, highs, color='red', alpha=0.5)   # Plot high temps in red
ax.plot(dates, lows, color='blue', alpha=0.5)   # Plot low temps in blue
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # Shade area between highs and lows

# format plot
ax.set_title('Daily High and Low Temperatures, 2018', fontsize=24)  # Set the plot title
ax.set_xlabel('', fontsize=16)           # Set the x-axis label (empty)
fig.autofmt_xdate()                      # Format date labels diagonally
ax.set_ylabel('Temperature(F)', fontsize=16)  # Set the y-axis label
ax.tick_params(labelsize=16)              # Set tick label size

# plt.savefig('sitka_highs.png', bbox_inches='tight')  # Optionally save the plot to a file
plt.show()                                # Display the plot
