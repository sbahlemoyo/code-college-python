class Restaurant():
    """A class that represents a restaurant"""
    def __init__(self, name, cuisine_type):
        """Initializing variables to be used in restaurant class"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Info about restaurant"""
        print(f'Welcome to {self.name}')
        print(f'We offer {self.cuisine_type} style food.')

    def open_restaurant(self):
        print('We are currently open for business!')

    def num_served(self, num):
        self.number_served = num
        print(f"We've served {self.number_served} people.")

    def increment_num_served(self, increment):
        self.number_served += increment
        print(f'We\'ve now served {self.number_served} people.')