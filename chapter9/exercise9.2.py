class Restaurant:
    """A class that builds information about a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        

    def describe_restaurant(self):
        """Describes restaurant"""
        print(f"{self.restaurant_name.title()} is a  sophisticated restaurant offering {self.cuisine_type} type cuisine.")

    def open_restaurant(self):
        """Indicates open of restaurant"""
        print(f"{self.restaurant_name.title()} is open.")

    def set_number_served(self, num):
        ""
        self.number_served = num

    def increment_number_served(self, increment):
        self.number_served += increment
    

   
    
restaurant = Restaurant('Kota junction', 'african')
# print(restaurant.number_served)
# restaurant.number_served = 4
# print(restaurant.number_served)
# restaurant.set_number_served(6)
# print(restaurant.number_served)
restaurant.increment_number_served(18)
print(restaurant.number_served)

class User:
    """Class that creates a user profile"""
    def __init__(self, f_name, l_name, age,gender,  email):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.gender = gender
        self.email = email
        self.login_attempts

    def describe_user(self):
        """Displays information that describes user"""
        print(
            f"First Name: {self.first_name.title()}\nLast Name: {self.last_name.title()} \nAge: {self.age} \nGender: {self.gender.title()} \nEmail: {self.email}"
        )

    def greet_user(self):
        """Greets user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def rest_login_attempts(self):
        self.login_attempts = 0

user1 = User('sbahle', 'moyo', 24, 'female', 'sbahlem@company.com')
