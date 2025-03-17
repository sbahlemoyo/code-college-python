from pathlib import Path

path = Path('names.txt')
contents = path.read_text()

lines = contents.splitlines()
line_string = ' '
for line in lines:
    # print(line)
    line_string += line.lstrip()

# print(line_string)
# print(len(line_string))

my_name = input('Enter your name')
if my_name in line_string:
    print('Your name appears in this file')
else:
    print('Your name does not appear in this file.')


