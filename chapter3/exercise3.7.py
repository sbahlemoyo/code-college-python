invited_guests = ["mom", "dad", "sister", "brother"]
print(f'Hey {invited_guests[0]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[1]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[2]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[3]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(invited_guests[2])
invited_guests[2] = "Aunty"
print(f'Hey {invited_guests[0]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[1]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[2]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[3]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print('I have found a bigger table')
invited_guests.insert(0, "cousin")
invited_guests.insert(2, "uncle")
invited_guests.append("dog")
print(f'Hey {invited_guests[0]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[1]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[2]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[3]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[4]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[5]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')
print(f'Hey {invited_guests[6]}:\nI would like to invite you over for dinner.\nPlease RSVP so i can send you the deets.')


print('Due to insufficient space caused by a late dinner table\'s arrival, I can now only invite 2 guests.')
guest1 = invited_guests.pop()
print(f'Sorry {guest1}, i can no longer extend my invitation to dinner to you.')
guest2 = invited_guests.pop()
print(f'Sorry {guest2}, i can no longer extend my invitation to dinner to you.')
guest3 = invited_guests.pop()
print(f'Sorry {guest3}, i can no longer extend my invitation to dinner to you.')
guest4 = invited_guests.pop()
print(f'Sorry {guest4}, i can no longer extend my invitation to dinner to you.')
guest5 = invited_guests.pop()
print(f'Sorry {guest5}, i can no longer extend my invitation to dinner to you.')
print(invited_guests)


print(f"Hey {invited_guests[0]}, you're still invited for dinner")
print(f"Hey {invited_guests[1]}, you're still invited for dinner")

del invited_guests[0]
del invited_guests[0]
print(invited_guests)
