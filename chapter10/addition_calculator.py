def adding_numbers():
    """a function that adds two numbers provided by user"""
    # Start an infinite loop to keep asking for input until valid numbers are entered
    while True:
        try:
            # Prompt the user to enter the first number and convert it to an integer
            first_num = int(input('Enter 1st number: '))
            # Prompt the user to enter the second number and convert it to an integer
            second_num = int(input('Enter 2nd number: '))
        except ValueError:
            # If the user enters something that's not a number, print an error message
            print('The value you entered is not a number')
            # Continue the loop to ask for input again
            continue
        else:
            # If both inputs are valid numbers, print their sum
            print(first_num + second_num)
            # Exit the loop since the operation was successful
            break

# Call the function to start the calculator
adding_numbers()