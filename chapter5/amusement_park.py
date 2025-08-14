age = 12  # Set the age of the person

if age < 4:                  # Check if the age is less than 4
    price = 0                # Admission is free for ages under 4
elif age < 18:               # Check if the age is less than 18
    price = 25               # Admission is $25 for ages 4 to 17
elif age < 65:               # Check if the age is less than 65
    price = 40               # Admission is $40 for ages 18 to 64
elif age >= 65:              # Check if the age is 65 or older
    price = 20               # Admission is $20 for ages 65 and above

print(f"Your admission cost is ${price}.")  # Print
