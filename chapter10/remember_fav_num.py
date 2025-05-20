from pathlib import Path
import json

path = Path('favourite_num.json')
if path.exists():
    contents = path.read_text()
    user_info = json.loads(contents)
    print(f'Hello {user_info["name"].title()}. Your favourite number is {user_info["fav_num"]}')

else:
    ask_fav_num = input('What is your fav num?')
    ask_name = input('Enter your name:')
    ask_last_name = input('Enter your last name:')
    user_info = {'name': ask_name, 'surname': ask_last_name, 'fav_num': ask_fav_num}
    contents = json.dumps(user_info)
    path.write_text(contents)
