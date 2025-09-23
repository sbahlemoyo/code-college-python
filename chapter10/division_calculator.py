# Exceptions
# Handling the ZeroDivision Exception

try:
    # Try to divide 5 by 0, which will cause an error
    print(5/0)
except ZeroDivisionError:
    # If a division by zero occurs, print an error message
    print("You can't divide by zero!")

# Print instructions for the user
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

# Start an infinite loop to repeatedly ask for input
while True:
    # Ask the user to enter the first number
    first_number = input('\nEnter first number: ')
    # If the user enters 'q', exit the loop
    if first_number == 'q':
        break
    # Ask the user to enter the second number
    second_number = input('\nSecond number: ')
    # If the user enters 'q', exit the loop
    if second_number == 'q':
        break
    try:
        # Try to convert inputs to integers and divide them
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        # If the user tries to divide by zero, print an error message
        print("You can't divide by zero!")
    else:
        # If no error occurs, print the result of the division
        print(answer)
