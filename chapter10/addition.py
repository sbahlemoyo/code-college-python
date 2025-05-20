
def adding_numbers():
    """a function that adds two numbers provided by user"""
    try:
        prompt1 = int(input('Enter 1st number: '))
    except ValueError:
        print('The value you entered is not a number')
    else:
        try:
            prompt2 = int(input('Enter 2nd number: '))
        except ValueError:
            print('The value you entered is not a number')
        else:
            print(prompt1 + prompt2)

adding_numbers()




