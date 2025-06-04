from pathlib import Path                # Import the Path class for handling file paths
import csv                              # Import the csv module for reading CSV files

path = Path('weather_data/sitka_weather_07-2018_simple.csv')  # Create a Path object for the CSV file
lines = path.read_text().splitlines()    # Read the file's text and split it into a list of lines

reader = csv.reader(lines)               # Create a CSV reader object to parse the lines
header_row = next(reader)                # Get the first row from the CSV (the header row)

for index, column_header in enumerate(header_row):  # Loop through each column in the header row
    print(index, column_header)          # Print the index and name of each column


