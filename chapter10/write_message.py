# WRITING TO A A FILE

from pathlib import Path  # Import the Path class to work with file paths

# Create a string variable to hold the contents to write to the file
contents = 'I love programming.\n'
# Add another line to the contents string
contents += 'I love creating new games.\n'
# Add a third line to the contents string
contents += 'I also love working with data.\n'

# Create a Path object for the file 'programming.txt'
path = Path('programming.txt')
# Write the contents string to the file
path.write_text(contents)


