from random import randint
class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides + 1))

six_side_die = Die()
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()
# six_side_die.roll_die()
ten_side_die = Die(10)
twenty_side_die = Die(20)
ten_side_die.roll_die()
ten_side_die.roll_die()
ten_side_die.roll_die()
ten_side_die.roll_die()
ten_side_die.roll_die()
ten_side_die.roll_die()
ten_side_die.roll_die()
ten_side_die.roll_die()
ten_side_die.roll_die()
ten_side_die.roll_die()
ten_side_die.roll_die()
ten_side_die.roll_die()