# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

#ACCESSING AN IITEM ON THE LIST

# # motorcycles[0] = 'ducati'
# # print(motorcycles)

#APPENDING AN ITEM TO THE END OF A LIST

# motorcycles.append('ducati')
# print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

#INSERTING AN ITEM IN A PARTICULAR PART/INDEX IN A LIST

# print(motorcycles)
# motorcycles.insert(1, 'ducati')
# print(motorcycles)

#PERMANENTLY REMOVING AN ITEM FROM A LIST

# del motorcycles[0]
# print(motorcycles)

#USING POP METHOD TO REMOVE AN ITEM AT THE END OF A LIST
motorcycles.pop()
print(motorcycles)
#REMOVING WITH POP BY INDEX
motorcycles.pop(0)
print(motorcycles)

#REMOVING AN ITEM BY VALUE
motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

#INDEX ERRORS (--OUT OF RANGE--)
print(motorcycles[4])

#PRINTING LAST ITEM IN THE LIST
print(motorcycles[-1])


