pizza_toppings = "Enter your choice of pizza topping."
pizza_toppings += "\nEnter 'quit' to end your order"

topping = ""
while topping != "quit":
 topping = input(pizza_toppings)
 if topping != 'quit':
  print(f'Adding {topping} to your pizza...')


ask_age = input('What is your age?')
active = True
while active:
 ask_age = int(ask_age)
if ask_age < 3:
   print('Your ticket is free.')
   active = False
elif ask_age >=3 and ask_age < 12:
   print('Ticket is $10')
   active = False
elif ask_age >= 12:
   print('Ticket is $15')
   active = False