freind1 = {
    'firstname':'Kobe',
    'lastname':'Bryant',
    'age':'45'
}
friend2 = {
    'firstname':'Jaden',
    'lastname':'Smith',
    'age': 26
}
friend3 = {
    'firstname':'Selena',
    'lastname':'Gomez',
    'age': 33
}
friends = []
friends.append(freind1)
friends.append(friend2)
friends.append(friend3)
for friend in friends:
    for key, value in friend.items():
        print(f'{key.title()}:{value}')

