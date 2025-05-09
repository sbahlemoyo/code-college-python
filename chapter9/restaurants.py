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
