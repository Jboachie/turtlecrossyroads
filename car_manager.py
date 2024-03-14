COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1,2)
        self.setheading(180)
        self.penup()
        self.goto((random.randint(-250,250),(random.randint(-250,250))))
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT

    def car_stop(self):
        self.starting_move_distance = 0
        self.move_increment = 0

    def move_forward(self):
        self.new_x = self.xcor() - self.starting_move_distance
        self.new_y = self.ycor()
        self.goto(self.new_x, self.new_y)

    def off_screen_reset(self):
        self.goto(300, random.randint(-250,280))
