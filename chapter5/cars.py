cars = ['audi', 'bmw', 'subaru', 'toyota']  # Create a list of car brands
for car in cars:                            # Loop through each car in the list
    if car == 'bmw':                        # Check if the current car is 'bmw'
        print(car.upper())                  # Print 'bmw' in uppercase letters
    else:                                   # If the car is not 'bmw'
        print(car.title())                  # Print the car name with the first
