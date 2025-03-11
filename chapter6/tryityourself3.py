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

pet1 = {'type': 'dog',
         'owner': 'lucy',
         'food': 'bones',
         'toy': 'disk'}
pet2 = {'type': 'cat',
        'owner': 'grace',
        'food': 'fishbones',
        'toy': 'yarn'}
pet3 = {'type': 'mouse',
        'owner': 'adam',
        'food': 'cheese',
        'toy': 'mousetrap'}
pets = []
pets.append(pet1)
pets.append(pet2)
pets.append(pet3)
for pet in pets:
    for creature, info in pet.items():
        print(creature.title() + " : " + info.title())

favourite_places = {
    'Amy':'Bali',
    'Hannah': 'London',
    'Lucas': 'Paris',
    'Emmet': 'Rio',
    'Graham': 'Peurto Rico'
}
for person, location in favourite_places.items():
    print(f'{person.title()}\'s favourite place to be is {location}\n')
