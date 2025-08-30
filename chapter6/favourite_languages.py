#dictionary of similar objects
favourite_lang = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}
#looping through all keys
friends = ['phil', 'sarah']
for name in favourite_lang.keys():
    print(name.title())
    #utilising if statements with dictionaries
    if name in friends:
        language = favourite_lang[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#looping through all key-value pairs
for name, language in favourite_lang.items():
    print(f'{name.title()}\'s favourite language is {language}.')

if 'erin' not in favourite_lang:
    print('Hey Erin, please take our poll.')

#more complex example
for name in sorted(favourite_lang.keys()):
    print(name.title())
    #utilising if statements with dictionaries and lists
    if name in friends:
        language = favourite_lang[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#looping through all the values and using set if there is a repeat of an already mentioned language in the poll answers
print('The following languages have been mentioned:')
for language in set(favourite_lang.values()):
    print(language.title())

#lists inside of dictionaries
favourite_languages = {
    'jen': ['python', 'rust'],
    'sarah': 'c'
}
print(favourite_languages['jen'][0])






