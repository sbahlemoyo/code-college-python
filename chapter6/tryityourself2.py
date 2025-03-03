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


