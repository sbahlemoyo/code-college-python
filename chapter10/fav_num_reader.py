from pathlib import Path  # Import the Path class to work with file paths
import json  # Import the json module to handle JSON data

path = Path('favourite_num.json')  # Create a Path object for the JSON file
contents = path.read_text()  # Read the contents of the file as a string
fav_num = json.loads(contents)  # Convert the JSON string to a Python object

print(f'You\'re favourite number is {fav_num}')  # Print the favorite number to the user
