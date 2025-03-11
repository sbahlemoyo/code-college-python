glossary ={
    'variable':'any word you can assign a value',
    'data_type':'a form that datacomes in',
    'list':'a list of data stored inside square brackets'
}
print("Glossary:\t")
for definition, meaning in glossary.items():
    print(f'{definition}:\t{meaning}\n')

rivers = {
    'nile':'egypt',
    'umngeni':'south africa',
    'mississipi':'united states'
}
for river, country in rivers.items():
    print(f'The {river.title()} flows through {country.title()}.')

for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
'edwin': 'javascript',
'frank': 'javascript',
'lwandle': 'c'
}

poll_takers = ['phil', 'aaron', 'frank', 'john', 'jen', 'leisl', 'sandra']

for takers in poll_takers:
    if takers in favorite_languages.keys():
        print(f'Hey {takers.title()}, thank you for taking our poll')
    else:
        print(f"Hey {takers.title()}, we'd like to invite you to answer our poll")



