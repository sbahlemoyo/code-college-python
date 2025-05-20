from pathlib import Path
import json

path = Path('favourite_num.json')
if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f'Received. You\'re favourite number is {fav_num}')

else:
    ask_fav_num = input('What is your fav num? ')
    contents = json.dumps(ask_fav_num)
    path.write_text(contents)
