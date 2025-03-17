guest_name = input('Enter your name: ')
from pathlib import Path

guest = Path('guests.txt')


guest.write_text(guest_name.title())

print(guest_name)