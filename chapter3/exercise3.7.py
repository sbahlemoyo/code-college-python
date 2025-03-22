guests = ['mom', 'dad', 'sister', 'brother', 'niece', 'nephew', 'grandma', 'grandpa']
print(f"Dear {guests[0].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[1].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[2].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[3].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[4].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[5].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[6].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[7].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")

print(F'It seems {guests[3].title()}, won\'t be able to make it')
guests[3] = 'aunt'

print(f"Dear {guests[0].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[1].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[2].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[3].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[4].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[5].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[6].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[7].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")

print('I have found a bigger dinner table for us all.')

guests.insert(0, 'uncle')
guests.insert(3, 'cousin')
guests.append('friend')

print(f"Dear {guests[0].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[1].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[2].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[3].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[4].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[5].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[6].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[7].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[8].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[9].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")
print(f"Dear {guests[10].title()}, I'd like to invite you to dinner. Your presence would be appreciated.")

print('Unfortunately, due to late arrival of the dinner table i can now only host 2 guests for dinner.')

guest = guests.pop()
print(f'Sorry {guest.title()}, this will not happen again.')
guest = guests.pop()
print(f'Sorry {guest.title()}, this will not happen again.')
guest = guests.pop()
print(f'Sorry {guest.title()}, this will not happen again.')
guest = guests.pop()
print(f'Sorry {guest.title()}, this will not happen again.')
guest = guests.pop()
print(f'Sorry {guest.title()}, this will not happen again.')
guest = guests.pop()
print(f'Sorry {guest.title()}, this will not happen again.')
guest = guests.pop()
print(f'Sorry {guest.title()}, this will not happen again.')
guest = guests.pop()
print(f'Sorry {guest.title()}, this will not happen again.')
guest = guests.pop()
print(f'Sorry {guest.title()}, this will not happen again.')

print(f"Hello {guests[0].title()}, you are still invited for dinner.")
print(f"Hello {guests[1].title()}, you are still invited for dinner.")

del guests[1]
del guests[0]
print(guests)
