# Import the Path class from the pathlib module to work with file paths
from pathlib import Path

# Define a function to print the contents of a file
def print_contents(filepath):
    """prints file contents"""
    try:
        # Try to read the contents of the file
        contents = filepath.read_text()
    except FileNotFoundError:
        # If the file is not found, print an error message
        print(f'The file {filepath} is missing.')
        # pass  # This line is commented out; it would do nothing if uncommented
    else:
        # If the file is found, print its contents
        print(contents)

# Create a list of filenames to check
filenames = ['cats.txt', 'dogs.txt', 'birds.txt']

# Loop through each filename in the list
for filename in filenames:
    # Create a Path object for the current filename
    path = Path(filename)
    # Call the function to print the contents of the file
    print_contents(path)