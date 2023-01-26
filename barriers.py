import random
import turtle
from turtle import Turtle
import time

class Barrier(Turtle):

    def __init__(self):
        super().__init__()
        self.barriers = []


    def create_barrier(self):
        turtle.tracer(2, 0)
        time.sleep(1)
        x = 200
        for n in range(24):
            if n > 10:
                y = -120
            else:
                y = -150
            new_barrier = Turtle('square')
            new_barrier.speed("fastest")
            new_barrier.penup()
            new_barrier.right(90)
            new_barrier.color('yellow')
            new_barrier.goto(x, y)
            self.barriers.append(new_barrier)
            if n > 10:
                x = x + random.randint(0, 100)
            else:
                x = x - random.randint(0, 100)
