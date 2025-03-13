colour = "red"
print("is colour == red? i predict true")
print(colour == "red")
print("is colour == blue? i predict false")
print(colour == "blue")
print("is colour == Red? i predict false")
print(colour == "Red")

print(colour != "red")
print(colour.title() == "Red")
print(colour.lower() == 'red')

num = 15
print(num > 15)
print(num < 15)
print(num == 15)
print(num > 20 and num < 30)
print(num >= 15 or num < 10 )

clothes = ["jeans", "hat", "shoes", "shorts", "dress"]
print("hat" in clothes)
print("watch" not in clothes)
print('hat' not in clothes)