fav_pizza = ["pepperoni", "pineapple", "chicken and cheese", "sticky bbq"]
for pizza in fav_pizza:
    print(f'I love me a good old {pizza} pizza!')
print(f"I like different kinds of pizzas such as:\n{fav_pizza[0]}, {fav_pizza[1]}, {fav_pizza[2]}, {fav_pizza[3]}")
print(f'The first three items on the list are:\n{fav_pizza[:3]}')
print(f'The items in the middle of the list are:\n{fav_pizza[1:3]}')
print(f'The last three items on the list are:\n{fav_pizza[-3:]}')
duplicate_pizzas = fav_pizza[:]
duplicate_pizzas.append("feta and cheese")
fav_pizza.append("mexican fiesta")
print(f'My favourite pizzas are:/n')
for piz in fav_pizza:
    print(piz.title())
print(f'My favourite pizzas are:/n')
for flav in duplicate_pizzas:
    print(flav.title())
