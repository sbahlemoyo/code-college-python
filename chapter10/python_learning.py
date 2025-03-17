from pathlib import Path

my_path = Path('learning_python.txt')
new_content = my_path.read_text()
 
# lines2 = ''
# # # for i in range(2):
# # #     print(new_content)
# for lines in lines1:
#     lines2 += lines

# print(lines2)


for lines in new_content.splitlines():
    modified_line = lines.replace('Python', 'C')
    print(modified_line)
    


