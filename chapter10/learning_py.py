from pathlib import Path
path = Path('learning_python.txt')
# contents = path.read_text()
# print(contents)
# contents = path.read_text().splitlines()
# for line in contents:
#     print(line)

# lines = contents.splitlines()
# for line in lines:
#     if 'python' in line:
#         line = line.replace('python', 'C')
#         print(line)

contents = path.read_text().splitlines()
for line in contents:
    if 'python' in line:
       line = line.replace('python', 'C')
    print(line)

