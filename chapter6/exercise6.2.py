glossary = {
    'variable': 'A container for storing data values.',
    'function': 'Reusable block of code.',
    'loop': 'Executes a block of code repeatedly.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'if statement': 'Executes code based on a condition.',
    'elif': 'Stands for else-if, for multiple condition checks.',
    'boolean': 'A data type that can be True or False.',
    'string': 'A series of characters.',
    'input': 'A function to get user data.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")


#rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}

for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

print("\nRivers included in the dictionary:")
for river in rivers:
    print(f"- {river.title()}")

print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(f"- {country.title()}")


#poll
favorite_languages = {
    'alice': 'python',
    'bob': 'c',
    'charlie': 'java',
    'diana': 'ruby'
}

people_to_poll = ['alice', 'bob', 'zuko', 'thando', 'diana']

for person in people_to_poll:
    if person.lower() in favorite_languages:
        print(f"Thank you for responding, {person.title()}!")
    else:
        print(f"{person.title()}, please take the poll about your favorite language!")

