
def adding_numbers():
    """a function that adds two numbers provided by user"""
    while True:
        try:
            first_num = int(input('Enter 1st number: '))
            second_num = int(input('Enter 2nd number: '))
        except ValueError:
            print('The value you entered is not a number')
            continue
        else:
           print(first_num + second_num)
           break

adding_numbers()