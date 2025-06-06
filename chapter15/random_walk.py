from random import choice #Imports the function to make random decisions

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points #How many steps the walk will take

        #All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        #Keep taking step until we reach the desired length
        while len(self.x_values) < self.num_points:

            #Decide direction and distance for each axis
            x_direction = choice([1, -1]) #step left or right
            x_distance = choice([0, 1, 2, 3, 4]) #how far to step
            x_step = x_direction * x_distance #signed step


            y_direction = choice([1, -1]) #step left or right
            y_distance = choice([0, 1, 2, 3, 4]) #how far to step
            y_step = y_direction * y_distance #signed step

            #Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #Calcu;ate new position
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            #Append new step to the walk
            self.x_values.append(next_x)
            self.y_values.append(next_y)