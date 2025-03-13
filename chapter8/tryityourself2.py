def make_shirt(size='L' , message='I LOVE PYTHON'):
    """ Making a shirt using size and message to be printed"""
    print(f'Shirt details:\nSize : {size}\nMessage : {message}')

make_shirt('M', 'Python is great and easy to use!')
make_shirt(size='M', message='Python is great and easy to use!')
make_shirt()


def describe_city(city, country='south africa'):
    """ Printing a city and the country it's found in"""
    print(f'{city.title()} is in {country.title()}')

describe_city('johannesburg')
describe_city('durban')
describe_city('lagos')



