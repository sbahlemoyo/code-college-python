person1 = {'first_name': 'Lwazi', 'last_name': 'Nkosi', 'age': 25, 'city': 'Durban'}
person2 = {'first_name': 'Zara', 'last_name': 'Khumalo', 'age': 30, 'city': 'Johannesburg'}
person3 = {'first_name': 'Neo', 'last_name': 'Mokoena', 'age': 22, 'city': 'Cape Town'}

people = [person1, person2, person3]

for person in people:
    print(f"\nPerson:")
    for key, value in person.items():
        print(f"  {key.title()}: {value}")

#pets
pet1 = {'animal': 'dog', 'owner': 'Amahle'}
pet2 = {'animal': 'cat', 'owner': 'Siyabonga'}
pet3 = {'animal': 'parrot', 'owner': 'Thuli'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\nPet Info:")
    for key, value in pet.items():
        print(f"  {key.title()}: {value}")

#favorite places
favorite_places = {
    'Lindiwe': ['Paris', 'Zanzibar'],
    'Musa': ['Tokyo', 'Seoul', 'Cape Town'],
    'Tebogo': ['New York']
}

for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places:")
    for place in places:
        print(f"  - {place}")

#favourite number
favorite_numbers = {
    'Zanele': [7, 14],
    'Bongani': [3, 9, 27],
    'Naledi': [1],
    'Thabo': [5, 10],
    'Karabo': [8, 13]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers:")
    for num in numbers:
        print(f"  - {num}")

#cities
cities = {
    'cape town': {
        'country': 'south africa',
        'population': '4 million',
        'fact': "It's home to Table Mountain."
    },
    'nairobi': {
        'country': 'kenya',
        'population': '4.4 million',
        'fact': 'It has a national park within the city.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '37 million',
        'fact': 'It\'s the world\'s largest metro area.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    for key, value in info.items():
        print(f"  {key.title()}: {value}")


