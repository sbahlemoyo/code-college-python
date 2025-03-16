# class Restaurant():
#     """A class that represents a restaurant"""
#     def __init__(self, name, cuisine_type):
#         """Initializing variables to be used in restaurant class"""
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
    
#     def describe_restaurant(self):
#         """Info about restaurant"""
#         print(f'Welcome to {self.name}')
#         print(f'We offer {self.cuisine_type} style food.')

#     def open_restaurant(self):
#         print('We are currently open for business!')

#     def num_served(self, num):
#         self.number_served = num
#         print(f"We've served {self.number_served} people.")

#     def increment_num_served(self, increment):
#         self.number_served += increment
#         print(f'We\'ve now served {self.number_served} people.')

# restaurant1 = Restaurant('La vida loca', 'mexican')
# print(restaurant1.name)
# print(restaurant1.cuisine_type)
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()

# restaurant2 = Restaurant('Wakanda', 'african')
# restaurant3 = Restaurant('Ji Chen', 'Asian')
# restaurant4 = Restaurant('Paradise Hill', 'mediterranian')
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()
# print('\n')
# restaurant3.describe_restaurant()
# restaurant3.open_restaurant()

# restaurant = Restaurant('ji chen', 'asian')
# print(restaurant.number_served)
# restaurant.num_served(50)
# restaurant.increment_num_served(12)

# class Icecreamstand(Restaurant) :
#     """Creating a restaurant child class named Icecreamstand"""
#     def __init__(self, name, cuisine_type, flavors):
#         """Initialising parent attributes in child class(Icecreamstand)"""
#         super().__init__(name, cuisine_type)
#         self.flavours = flavors 

#     def display_flavours(self):
#         print('We offer the following flavors:')
#         for option in self.flavours:
#             print(f'{option.title()}')

# icecreamstand = Icecreamstand('bruno\'s', 'ice cream',['chocolate', 'vanilla', 'caramel', 'fudge','strawberry'])
# icecreamstand.display_flavours()








