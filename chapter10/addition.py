def adding_numbers():
    """a function that adds two numbers provided by user"""
    # Try to get the first number from the user
    try:
        # Ask the user to enter the first number and convert it to an integer
        prompt1 = int(input('Enter 1st number: '))
    except ValueError:
        # If the input is not a valid integer, print an error message
        print('The value you entered is not a number')
    else:
        # If the first input is valid, try to get the second number
        try:
            # Ask the user to enter the second number and convert it to an integer
            prompt2 = int(input('Enter 2nd number: '))
        except ValueError:
            # If the input is not a valid integer, print an error message
            print('The value you entered is not a number')
        else:
            # If both inputs are valid, print their sum
            print(prompt1 + prompt2)

# Call the function to start the calculator
adding_numbers()




