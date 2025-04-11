car = input("What kind of rental car would you like? ")

print(f"Let me see if I can find you a {car.title()}.")

#restaurant seating
group_size = int(input("How many people are in your dinner group? "))

if group_size > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Your table is ready. Follow me!")

#multiples of ten
number = int(input("Enter a number, and I'll tell you if it's a multiple of 10: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
