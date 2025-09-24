from pathlib import Path  # Import the Path class to work with file paths
import json  # Import the json module to handle JSON data

path = Path('numbers.json')  # Create a Path object for the file 'numbers.json'
contents = path.read_text()  # Read the contents of the file as a string
numbers = json.loads(contents)  # Convert the JSON string back into a Python list

print(numbers)  # Print the list of numbers to the screen