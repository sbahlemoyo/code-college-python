from pathlib import Path

guest_book = Path('guest_book.txt')
guests = []
while True:
    guest_names = input('Welcome guest, please senter your name("q" to stop): ')
    
    if guest_names.lower() == 'q':
        print('Exiting guest name portal...')
        break
    else:
        guests.append(guest_names.title())

with guest_book.open("a") as file:
    for guest in guests:
        file.write(guest + "\n")  # Append each name on a new line

print("Guest names have been saved to guest_book.txt!")
        
        

    

