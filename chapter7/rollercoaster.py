###Using int() to accept numerical input
###By default the input function returns string data and if your program compares data from an input function to numerical data, it will give an error. So it is important to convert string data from the input function to numerical data. 

height = input("How tall are you, in inches?")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older")