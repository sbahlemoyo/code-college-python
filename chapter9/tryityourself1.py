class Restaurant:
    """A class that builds information about a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes restaurant"""
        print(f"{self.restaurant_name.title()} is a  sophisticated restaurant offering {self.cuisine_type} type cuisine.")

    def open_restaurant(self):
        """Indicates open of restaurant"""
        print(f"{self.restaurant_name.title()} is open.")

restaurant= Restaurant('Minos', 'mediterranian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant('MaxVillage', 'african')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('La vida loca', 'mexican')
restaurant4 = Restaurant('Chi do', 'korean')
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()


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

user1 = User('sbahle', 'moyo', 24, 'female', 'sbahlem@company.com')
user1.describe_user(
)
user1.greet_user()