names = ['sbahle', 'asanda', 'nompilo', 'nokwazi', 'siyabonga', 'wandile', 'melokuhle', 'jason', 'unami', 'uminathi', 'liyana']

print(f'The first three names in the list are: ')
for name in names[:3]:
    print(name.title())

print('\nThree items from the middle of the list are: ')
for name in names[4:7]:
    print(name.title())

print('\nThe last three items in the list are: ')
for name in names[-3:]:
    print(name.title())

pizzas = ['feta and cheese', 'bacon and pineapple', 'mexican fiesta']
friend_pizzas = pizzas[:]
pizzas.append('olive and feta')
friend_pizzas.append('chicken')

print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza.title())

print('\nMy friends favorite pizzas are: ')
for pizza in friend_pizzas:
    print(pizza.title())


