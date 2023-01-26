import random
import turtle
from turtle import Turtle
import time

class Aliens(Turtle):

    def __init__(self):
        super().__init__()
        self.aliens = []
        self.all_bullets_ets = []

    def create_aliens(self):
        turtle.tracer(2, 0)
        time.sleep(1)
        x = 120
        for n in range(24):
            if n > 10:
                y = 220
            else:
                y = 250
            new_alien = Turtle('turtle')
            new_alien.speed("fastest")
            new_alien.penup()
            new_alien.right(90)
            new_alien.color('white')
            new_alien.goto(x, y)
            self.aliens.append(new_alien)
            if n > 10:
                x = x + 30
            else:
                x = x - 30

    def move_aliens(self, move_variable, side):

        for et in self.aliens:
            x, y = et.pos()
            if move_variable < 10:
                et.goto(x+(10*side), y)
            else:
                et.goto(x, y-10)


    def shoot_aliens(self):
        if random.choice((1, 2, 3, 4, 5)) == 5:
            choice = random.choice(self.aliens)
        else:
            return None

        self.shoot = Turtle(shape='circle')
        self.shoot.hideturtle()
        self.shoot.penup()
        self.shoot.shapesize(0.25)
        self.shoot.color('white')
        self.shoot.goto(choice.xcor(), choice.ycor())
        self.shoot.showturtle()
        self.all_bullets_ets.append(self.shoot)


    def bullets_move(self):
        for bullet in self.all_bullets_ets:
            bullet.setheading(270)
            bullet.forward(10)


