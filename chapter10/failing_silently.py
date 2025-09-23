from pathlib import Path  # Import the Path class to work with file paths

def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        contents = path.read_text(encoding='utf-8')  # Try to read the contents of the file using UTF-8 encoding
    except FileNotFoundError:
        pass #nothing happens, no traceback message, no response is provided to the error, the programme skips over to the next iteration
    else:
        # Count the approximate number of words in the file.
        words = contents.split()  # Split the contents into a list of words
        num_words = len(words)  # Count the number of words in the list
        print(f"The file {path} has about {num_words} words.")  # Print the word count to the user

filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]  # List of filenames to process

for filename in filenames:  # Loop through each filename in the list

    path = Path(filename)  # Create a Path object for the current filename
    count_words(path)  # Call the function to count words in the current file