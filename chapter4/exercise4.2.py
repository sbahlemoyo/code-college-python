for num in range(1, 21):
    print(num)

for num in range(1, 1_000_001):
    print(num)

numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1, 20, 2))

for num in odd_numbers:
    print(num)

multiples_of_3 = list(range(3, 30, 3))
for multiple in multiples_of_3:
    print(multiple)


cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

#list comprehensions
another_cube = [cube**3 for cube in range(1,10)]
print(another_cube)


