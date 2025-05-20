from pathlib import Path
def print_contents(filepath):
    """prints file contents"""
    try:
        contents = filepath.read_text()
    except FileNotFoundError:
        print(f'The file {filepath} is missing.')
        # pass
    else:
        print(contents)

filenames = ['cats.txt', 'dogs.txt', 'birds.txt']
for filename in filenames:
    path = Path(filename)
    print_contents(path)