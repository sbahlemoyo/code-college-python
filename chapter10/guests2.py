from pathlib import Path
path = Path('guest_book.txt')
names = ''
while True: 
    
    guest_name = input('Enter your name(press q to exit): ')
    if guest_name != 'q':
        names += f"{guest_name}\n"
    else:
        break
    
path.write_text(names)  
    