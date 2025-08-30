# Using break to exit a loop

prompt = "\nPlease enter the city you have visited: "  # Create a prompt message for the user
prompt += "\n(Enter 'quit' when you are finished.)"    # Add instructions for quitting

while True:  # Start an infinite loop
    city = input(prompt)  # Get input from the user

    if city == 'quit':  # If the user enters 'quit'
        break  # Exit the loop
    else:
        print(f"I'd love to go to {city.title()}!")  # Print a message with the city name, formatted with title
