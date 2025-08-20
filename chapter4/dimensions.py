dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#throws an error because you can't change values in a tuple
# dimensions[0] = 250

#looping through all values in a tuple
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)


#The only way to edit or make changes to a tuple is to reassign it to a new tuple
dimensions = (400, 100)
print('/nModified dimensions: ')
for d in dimensions:
    print(d)