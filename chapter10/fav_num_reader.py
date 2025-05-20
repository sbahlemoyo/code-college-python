from pathlib import Path
import json

path = Path('favourite_num.json')
contents = path.read_text()
fav_num = json.loads(contents)

print(f'You\'re favourite number is {fav_num}')
