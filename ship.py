from turtle import Turtle
import turtle
import time

class Ship(Turtle):

    def __init__(self):
        super().__init__()
        turtle.tracer(2, 0)
        self.all_ships = []
        time.sleep(1)
        self.ship = Turtle(shape='turtle')
        self.ship.penup()
        self.ship.color('red')
        self.ship.goto(0, -250)
        self.ship.left(90)
        self.all_ships.append(self.ship)
        self.all_bullets = []
        self.x = self.ship.xcor()


    def move_left(self):
        self.x = self.x - 10
        self.ship.goto(self.x, -250)

    def move_right(self):
        self.x = self.x + 10
        self.ship.goto(self.x, -250)

    def shoot_now(self):

        self.shoot = Turtle(shape='circle')
        self.shoot.hideturtle()
        self.shoot.penup()
        self.shoot.shapesize(0.25)
        self.shoot.color('red')
        self.shoot.goto(self.ship.xcor(), -250)
        self.shoot.showturtle()
        self.all_bullets.append(self.shoot)

    def move_ship_bullet(self):
        for bullet in self.all_bullets:
            bullet.setheading(90)
            bullet.forward(25)




