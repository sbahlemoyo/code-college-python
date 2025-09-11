# Define a class named Dog to model a dog.
class Dog:
    """A simple attempt to model a dog."""

    # The __init__ method initializes the object's attributes.
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # Store the dog's name.
        self.name = name
        # Store the dog's age.
        self.age = age

    # Define a method to simulate the dog sitting.
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        # Print a message indicating the dog is sitting.
        print(f"{self.name} is now sitting.")

    # Define a method to simulate the dog rolling over.
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        # Print a message indicating the dog rolled over.
        print(f"{self.name} rolled over!")

# Create an instance of the Dog class with name 'Cassie' and age 9.
german_shepard = Dog('Cassie', 9)
# Print the name of the dog.

# Accessing Attributes
print(german_shepard.name)

# Calling methods
# Call the roll_over method to simulate the dog rolling over.
german_shepard.sit()
german_shepard.roll_over()

# Creating multiple instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(my_dog.name)
my_dog.sit()
print(your_dog.age)
your_dog.roll_over()

