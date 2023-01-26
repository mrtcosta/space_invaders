from turtle import Turtle

score = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.clear()
        self.penup()
        self.color("white")
        self.goto(-300, 250)
        self.write(f"Score: {score}", False, "left", font=("Courier", 25, "normal"))

    def score_up(self):
        global score
        self.clear()
        score += 1
        self.write(f"Score: {score}", False, "left", font=("Courier", 25, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=("Courier", 24, "bold"))