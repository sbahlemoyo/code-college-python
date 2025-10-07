# ###INHERITENCE##########  # This comment indicates the topic of inheritance in object-oriented programming.

from car import Car  # Import the Car class from another file to use as a base class.

class ElectricCar(Car):  # Define a new class ElectricCar that inherits from Car.
    """Represent aspects of a car, specific to electric vehicles"""  # Class docstring describing its purpose.

    def __init__(self, make, model, year):  # Initialize the ElectricCar object with make, model, and year.
        super().__init__(make, model, year)  # Call the parent class's initializer to set common attributes.
        self.battery_size = 40  # Define a new attribute specific to ElectricCar for battery size.

    def describe_battery(self):  # Define a method to describe the battery size.
        """Print a statement describing battery size"""  # Method docstring.
        print(f"This car has a {self.battery_size}-kWh battery.")  # Print the battery size.

    # Overriding parent method if it doesn't align with child class
    def fill_gas_Tank(self):  # Define a method that overrides the parent class's method.
        """Electric cars don't have gas tanks"""  # Method docstring.
        print("This car doesn't have a gas tank!")  # Print a message specific to electric cars.

my_leaf = ElectricCar('nissan', 'leaf', 2024)  # Create an instance of ElectricCar with specific details.
# print(my_leaf.get_descriptive_name())  # Print the car's descriptive name using a method from Car.
my_leaf.describe_battery()  # Print the battery details using the ElectricCar method.