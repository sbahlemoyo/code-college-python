def display_message():
    """"Printing a message describing what we are learning in this chapter """
    print('We are learning Python functions.')

display_message()

def favourite_book(title):
    """ Printing a sentence using a title of a book as a parameter"""
    print(f'One of my favourite books is "{title.title()}"')

favourite_book('the glass castle')