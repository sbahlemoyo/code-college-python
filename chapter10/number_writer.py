# Using json.dumps() and json.loads()

from pathlib import Path  # Import the Path class to work with file paths
import json  # Import the json module to handle JSON data

numbers = [2, 3, 5, 7, 11, 13]  # Create a list of numbers to store in a file

path = Path("numbers.json")  # Create a Path object for the file 'numbers.json'
contents = json.dumps(numbers)  # Convert the list of numbers to a JSON-formatted string
path.write_text(contents)  # Write the JSON string to the file