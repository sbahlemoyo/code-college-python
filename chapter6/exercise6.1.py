person = {
    'first_name': 'Sbahle',
    'last_name': 'Mkhize',
    'age': 24,
    'city': 'Durban'
}

print(f"First Name: {person['first_name']}")
print(f"Last Name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

favorite_numbers = {
    'Anele': 7,
    'Zuko': 3,
    'Nomvula': 10,
    'Sbahle': 5,
    'Lerato': 22
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of code that only runs when it is called.',
    'loop': 'A way to repeat a block of code multiple times.',
    'list': 'An ordered collection of items.',
    'dictionary': 'A collection of key-value pairs.'
}

print(f"Variable : \n\t{glossary['variable']}")
print(f"\nFunction: \n\t{glossary['function']}")
print(f"\nLoop: \n\t{glossary['loop']}")
print(f"\nList: \n\t\{glossary['list']}")
print(f"\nDictionary: \n\t{glossary['dictionary']}")
