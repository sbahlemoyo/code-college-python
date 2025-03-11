fav_pizza = ["pepperoni", "pineapple", "chicken", "cheese", "sticky bbq"]
print(f'The first three items on the list are:\t')
for flavour in fav_pizza[:3]:
    print(flavour.title())

print('Three items from the middle of the list are:\t')
for flav in fav_pizza[2:]:
    print(flav.title())

print('The last three items in the list are:\t')
for last_flav in fav_pizza[-3:]:
    print(last_flav.title())

friend_pizzas = fav_pizza[:]
fav_pizza.append("feta and cheese")
friend_pizzas.append("mushroom")
print("My favourite pizzas are:\t")
for piz in fav_pizza:
    print(piz.title())
print("My friend's favourite pizzas are:\t")
for friend_fav in friend_pizzas:
    print(friend_fav.title())