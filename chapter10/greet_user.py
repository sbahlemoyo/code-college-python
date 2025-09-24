from pathlib import Path  # Import the Path class to work with file paths
import json  # Import the json module to handle JSON data

path = Path('username.json')  # Create a Path object for the file 'username.json'
contents = path.read_text()  # Read the contents of the file as a string
username = json.loads(contents)  # Convert the JSON string back into a Python string (the username)

print(f"Welcome back, {username}!")  # Print a welcome message to the user using their stored name