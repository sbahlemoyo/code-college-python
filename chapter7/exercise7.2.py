prompt = "\nEnter a pizza topping you'd like (or 'quit' to finish): "

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza!")

#movie tickets
while True:
    age_input = input("\nEnter your age (or type 'quit' to stop): ")
    if age_input.lower() == 'quit':
        break
    
    age = int(age_input)
    
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

#three exits

#conditional
topping = ""
while topping.lower() != 'quit':
    topping = input("Add a topping (type 'quit' to stop): ")
    if topping.lower() != 'quit':
        print(f"Adding {topping} to your pizza.")

#active variable
active = True
while active:
    topping = input("Topping (or 'quit'): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping}.")

#break statement
while True:
    topping = input("Enter topping (or 'quit'): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping}.")

#infinity

while True:
    print("This loop will run forever... until you stop it manually! 💀")
