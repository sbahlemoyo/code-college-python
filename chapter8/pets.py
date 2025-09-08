#Positional Arguments

def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# #Multiple function calls using the same function for a different output
# describe_pet('dog', 'willie')

# #Order matters in positional arguments
# describe_pet('harry', 'hamster')

# #Keyword Arguments(name-value pair passed in a function and it directly associates the name and the value within the argument)
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

# #Default values
# describe_pet(pet_name='Willie')

#EquivelANT Function calls

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#Avoiding Arguments
describe_pet()

