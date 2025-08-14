#Lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing elements in a list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

print(bicycles[0].title())#We can use string methods on string elements in a list but not on numbers

#Index position starts at 0, not 1

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])#Prints the last item in a list

#Using Individual Values from a list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
