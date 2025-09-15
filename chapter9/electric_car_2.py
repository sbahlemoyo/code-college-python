from car import Car  # Import the Car class from another file to use as a base class.

class Battery:  # Define a new class to model a battery for an electric car.
    """A simple attempt to model a battery  for an electric car."""

    def __init__(self, battery_size=40):  # Initialize the Battery object with a default size.
        """Initialize the battery's attributes."""
        self.battery_size = battery_size  # Store the battery size as an attribute.

    def describe_battery(self):  # Method to display information about the battery.
        """Print statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery")  # Print the battery size.

    def get_range(self):
        """Print a statement about the range a battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):  # Define a new class for electric cars, inheriting from Car.
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):  # Initialize the ElectricCar object.
        super().__init__(make, model, year)  # Call the parent class's initializer.
        self.battery = Battery()  # Create a Battery instance as an attribute of ElectricCar.

my_leaf = ElectricCar('nissan', 'leaf', 2024)  # Create an ElectricCar object with specific details.
print(my_leaf.get_descriptive_name())  # Print the car's descriptive name using a method from Car.
my_leaf.battery.describe_battery()  # Print the battery details using the Battery class method.
my_leaf.battery.get_range()