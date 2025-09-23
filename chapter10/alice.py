# Handling the FileNotFoundError exception

# Import the Path class from the pathlib module to work with file paths
from pathlib import Path

# Create a Path object for the file 'alice.txt'
path = Path('alice.txt')
try:
    # Try to read the contents of the file using UTF-8 encoding
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    # If the file does not exist, print an error message
    print(f"Sorry, the file {path} does not exist")
else:
    # If the file is found, split its contents into words
    words = contents.split()
    # Count the number of words in the list
    num_words = len(words)
    # Print the number of words found in the file
    print(f"The file {path} has about {num_words} words.")