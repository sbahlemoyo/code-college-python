from pathlib import Path  # Import the Path class to work with file paths

path = Path('pi_million_digits.txt')  # Create a Path object for the file with a million digits of pi
contents = path.read_text()  # Read the contents of the file as a single string
lines = contents.splitlines()  # Split the contents into a list of lines

pi_string = ''  # Initialize an empty string to hold all the digits of pi
for line in lines:
    pi_string += line.strip()  # Add each line to pi_string, removing leading/trailing whitespace

birthday = input("Enter your birthday, in the form mmddyy: ")  # Ask the user for their birthday in mmddyy format
if birthday in pi_string:  # Check if the birthday appears in the pi digits string
    print("Your birthday appears in in the first million digits of pi!")  # Inform the user if found
else:
    print("Your birthday does not appear in the first million digits of pi.")  # Inform the user if not found