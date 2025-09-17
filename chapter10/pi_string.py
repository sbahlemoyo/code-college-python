# WORKING WITH A FILE'S CONTENTS

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
# contents.rstrip()
# print(contents)

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
