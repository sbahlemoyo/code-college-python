from pathlib import Path
path = Path('learning_python.txt')
# contents = path.read_text()
# print(contents)
# contents = path.read_text().splitlines()
# for line in contents:
#     print(line)
contents = path.read_text().splitlines()
for sentence in contents:
    if 'python' in sentence:
       sentence = sentence.replace('python', 'C')
    print(sentence)

