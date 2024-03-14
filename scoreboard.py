FONT = ("Courier", 24, "normal")
SCORE = 1
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.score = SCORE
        self.write(f"Level: {self.score} ", align= 'left', font= FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"Level: {self.score} ", align='left', font=FONT)

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font= FONT)