# READING THE CONTENTS OF A FILE

from pathlib import Path  # Import the Path class to work with file paths

path = Path('pi_digits.txt')  # Create a Path object for the file 'pi_digits.txt'
contents = path.read_text()  # Read the contents of the file as a single string
# contents.rstrip()  # This line would remove trailing whitespace if uncommented
# print(contents)    # This line would print the raw file contents if uncommented

lines = contents.splitlines()  # Split the contents into a list of lines
for line in lines:  # Loop through each line in the list
    print(line)  # Print the current line