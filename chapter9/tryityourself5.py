######exercise9.13##########
class Die:
    """A class that creates a dice object"""
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        """Rolls die"""
        from random import randint
        random_num = randint(1, self.sides)
        print(random_num)

# roll = Die(6)
# roll.roll_die()
# roll.roll_die()
# roll.roll_die()
# roll.roll_die()
# roll.roll_die()
# roll.roll_die()
# roll.roll_die()
# roll.roll_die()
# roll.roll_die()
# roll.roll_die()
# roll.roll_die()
# roll2 = Die(10)
# roll2.roll_die()
# roll2.roll_die()
# roll2.roll_die()
# roll2.roll_die()
# roll2.roll_die()

######exercise9.14######

num = [10, 'a', 7, 'f', 9, 'r', 3, 'o', 4, 6, 2, 1, 5, 8, 'l']
from random import choice
# ticket = []
# while len(ticket)< 4:
#     select = choice(num)
#     ticket.append(select)

# print('Any ticket matching the ffg numbers or letters wins:')
# print(ticket)

#####exeercise9.15#####

my_ticket = ['a', 7, 'l', 3]
counter = 0
while True:
    ticket = []
    while len(ticket)<4:
        select = choice(num)
        ticket.append(select)
    if my_ticket == ticket:
        print(f"Congratulations you won the lottery! It took you {counter} attempts to win." )
        break
    else:
        counter += 1
        
    
    
    

