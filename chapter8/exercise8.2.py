def make_shirt(size, message):
    print(f"The shirt size is {size.upper()} and it will say: '{message}'.")


make_shirt('medium', 'Keep calm and code Python.')

make_shirt(message='Born to debug.', size='large')

#large shirts
def make_shirt(size='large', message='I love Python'):
    print(f"The shirt size is {size.upper()} and it will say: '{message}'.")

make_shirt()

make_shirt(size='medium')

make_shirt('small', 'Python > Everything')

#cities
def describe_city(city, country='South Africa'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('cape town')
describe_city('durban')

describe_city('tokyo', 'japan')

