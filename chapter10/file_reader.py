# READING THE CONTENTS OF A FILE

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
# contents.rstrip()
# print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)