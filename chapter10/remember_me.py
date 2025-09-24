# Saving and reading user-generated data

from pathlib import Path  # Import the Path class to work with file paths
import json  # Import the json module to handle JSON data

username = input("What is your name? ")  # Ask the user to enter their name and store it in the variable 'username'

path = Path('username.json')  # Create a Path object for the file 'username.json'
contents = json.dumps(username)  # Convert the username string to a JSON-formatted string
path.write_text(contents)  # Write the JSON string to the file

print(f"We'll remember you when you come back, {username}!")  # Print a message to the user confirming their name is saved
