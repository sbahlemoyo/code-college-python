# Define a class named Car to represent a car.
class Car:
    """A simple attempt to represent a car"""

    # The __init__ method initializes the car's attributes.
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make              # Store the car's make (manufacturer).
        self.model = model            # Store the car's model.
        self.year = year              # Store the car's manufacturing year.
        self.odometer_reading = 30    # Set a default value for the odometer reading.

        # We can modify this attribute directly if needed.
        # self.odometer_reading = 23

    # Define a method to get a descriptive name for the car.
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"  # Create a formatted string with car details.
        return long_name.title()                              # Return the string in title case.
    
    # Define a method to display the car's mileage.
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")  # Print the current odometer reading.
    
    # Define a method to update the odometer reading.
    def update_odometer(self, mileage):
        """Set the odometer reading to given value
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:      # Check if the new mileage is not less than the current reading.
            self.odometer_reading = mileage       # Update the odometer reading.
        else:
            print("You can't roll back the odometer!")  # Print a warning if trying to decrease the mileage.

    # Define a method to increment the odometer reading.
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles            # Add the specified miles to the odometer.
    
# Create an instance of the Car class with specific details.
my_new_car = Car('audi', 'a4', 2024)
# Print the descriptive name of the car.
# print(my_new_car.get_descriptive_name())
# Update the odometer reading to 23 miles.
# my_new_car.update_odometer(23)

# # Display the car's current mileage.
my_new_car.read_odometer()