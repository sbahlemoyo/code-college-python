motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Modifying an element in a list

motorcycles[0] = 'ducati'
print(motorcycles)


#####Adding Elements to a list#####
#APPENDING AN ITEM TO THE END OF A LIST

motorcycles.append('ducati')#Append adds the element to the end of the list
print(motorcycles)

motorcycles = []#You can also append elements to an empty list for example a list that will store user responses after the submit them
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

####INSERTING AN ITEM IN A PARTICULAR PART/INDEX IN A LIST######

print(motorcycles)
motorcycles.insert(1, 'ducati')#inserts the element at index 1 and shifts all the elements that follow including the element that was at index 1
print(motorcycles)



#####PERMANENTLY REMOVING AN ITEM FROM A LIST######

#del motorcycles[0]#using the del statement
print(motorcycles)

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


