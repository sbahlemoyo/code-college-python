class Dog:
 """A simple attempt to model a dog."""
 def __init__(self, name, age):
  """Initialize name and age attributes."""
  self.name = name
  self.age = age

 def sit(self):
  """Simulate a dog sitting in response to a command."""
  print(f"{self.name} is now sitting.")

 def roll_over(self):
  """Simulate rolling over in response to a command."""
  print(f"{self.name} rolled over!")

german_shepard = Dog('Cassie', age=9)
print(german_shepard.name)
german_shepard.roll_over()
