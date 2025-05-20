from pathlib import Path
import json

favourite_num = input('Enter your favourite number: ')

path = Path('favourite_num.json')
contents = json.dumps(favourite_num)
path.write_text(contents)

