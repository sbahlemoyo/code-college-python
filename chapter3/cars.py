cars = ['bmw', 'audi', 'toyota', 'subaru']

#SORTING A LIST PERMANENTLY IN ALPHABETICAL ORDER
cars.sort()
print(cars)

#SORTING A LIST PERMANENTLY IN REVERSE ALPHABETICAL ORDER
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#TEMPORARILY SORTING A LIST IN ALPHABETICAL ORDER WITHOUT CHANGING THE ORIGINAL LIST ITSELF
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")#To show the original list has not changed
print(cars)

#PRINTING A LIST IN REVERSE
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#THE LENGTH OF A LIST
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))