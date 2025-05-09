############### EXERCISE 9.6##############
# class Restaurant:
#     """A class that builds information about a restaurant"""

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
        

#     def describe_restaurant(self):
#         """Describes restaurant"""

#         print(f"{self.restaurant_name.title()} is a  sophisticated restaurant offering {self.cuisine_type} type cuisine.")

#     def open_restaurant(self):
#         """Indicates open of restaurant"""

#         print(f"{self.restaurant_name.title()} is open.")

#     def set_number_served(self, num):
#         """Indicates number of people served"""

#         self.number_served = num

#     def increment_number_served(self, increment):
#         """Adds number of people served to the total of people served"""
#         self.number_served += increment

# class IceCreamStand(Restaurant):
#     """Class that creates Icecream restaurants"""
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ["chocolate", "caramel", "strawberry","vanilla", "tropical"]

#     def display_flavors(self):
#         """Displays Ice Cream flavors offered"""
        
#         print("We offer the following flavors:\n")
#         for flavor in self.flavors:
#             print(f"{flavor.title()}")

# Luigis = IceCreamStand('Luigi"s', "ice-cream")
# Luigis.display_flavors()

#######Exercise 9.7#############
class User:
    """Class that creates a user profile"""
    def __init__(self, f_name, l_name, age,gender,  email):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.gender = gender
        self.email = email

    def describe_user(self):
        """Displays information that describes user"""
        print(
            f"First Name: {self.first_name.title()}\nLast Name: {self.last_name.title()} \nAge: {self.age} \nGender: {self.gender.title()} \nEmail: {self.email}"
        )

    def greet_user(self):
        """Greets user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}")

class Administrator(User):
    """Class that creates administrator profile"""

    def __init__(self, f_name, l_name, age, gender, email):
        super().__init__(f_name, l_name, age, gender, email)
        self.privelages = Privelages()   

# admin1 = Administrator("Sbahle", "Moyo", 24, "female", "sbahle@company.site")
# admin1.show_privelages()

class Privelages:
    """Class storing admin privelages"""
    def __init__(self):
        self.privelages = ["can add post", "can delete post", "can ban user", "can access user info"]
    
    def show_privelages(self):
        """shows admin privelages"""
        print("These are your privelages as an admin: \n")
        for privelage in self.privelages:
            print(f"{privelage.capitalize()}")

admin1 = Administrator("Sbahle", "Moyo", 24, "female", "sbahle@company.site")
admin1.privelages.show_privelages()

########Exercise9.8############
class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 40

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")
