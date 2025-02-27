#for num in range(1, 21):
#    print(num)
#list1 = list(range(1, 1_000_000))
#print(min(list))
#print(max(list))
#print(sum(list))
odd = list(range(1, 21, 2))
print(odd)
for no in odd:
    print(no)
multiples = list(range(3, 30, 3))
for multiple in multiples:
    print(multiple)
empty = []
for digit in range(1, 10):
    cube = digit **2
    empty.append(cube)
    print(cube)
print(empty)
newlist = [digit **2 for digit in range(1, 11)]
print(newlist)
 
