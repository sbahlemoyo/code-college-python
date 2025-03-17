from random import choice
letters_and_num = [1, 'a', 5, 'd', 8, 'f', 0, 'l', 's', 4, 2, 6, 3, 9, 7]
winning_ticket = []
winning_ticket.append(choice(letters_and_num))
winning_ticket.append(choice(letters_and_num))
winning_ticket.append(choice(letters_and_num))
winning_ticket.append(choice(letters_and_num))

print(f'Any ticket matching these 4 characters wins the prize!: ')
print('-'.join(map(str, winning_ticket)))

