import random

class Dice:
    def roll(self):
        a = random.randint(1,6)
        b = random.randint(1,6)
        tuple_a = (a, b)
        print (tuple_a)

Student = Dice()
Student.roll()



