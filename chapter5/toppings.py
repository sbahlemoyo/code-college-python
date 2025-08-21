#checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")


#Checking whether a value is in a list
#And using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']  # List of toppings available in the shop

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']  # List of toppings requested by the customer

for requested_topping in requested_toppings:                        # Loop through each requested topping
    if requested_topping in available_toppings:                     # Check if the topping is available
        print(f"Adding {requested_topping}.")                       # Print message for adding the topping
    else:
        print(f"Sorry, we don't have {requested_topping}.")         # Print message if topping is not available
        
print("\nFinished making your pizza!")                              # Print final message


#Checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print('\n Finished making your pizza!')
else:
    print("Are you sure you want a plain pizza?")