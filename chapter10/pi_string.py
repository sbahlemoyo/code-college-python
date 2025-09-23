# WORKING WITH A FILE'S CONTENTS

from pathlib import Path  # Import the Path class to work with file paths

path = Path('pi_digits.txt')  # Create a Path object for the file 'pi_digits.txt'
contents = path.read_text()  # Read the contents of the file as a single string
# contents.rstrip()  # This line would remove trailing whitespace if uncommented
# print(contents)    # This line would print the raw file contents if uncommented

lines = contents.splitlines()  # Split the contents into a list of lines
pi_string = ''  # Initialize an empty string to hold the digits of pi

# Loop through each line in the list of lines
for line in lines:
    pi_string += line.lstrip()  # Add the line to pi_string, removing leading whitespace

print(pi_string)  # Print the combined string of pi digits
print(len(pi_string))  # Print the length of the pi_string to show how many digits there are
