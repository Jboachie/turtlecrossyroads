import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
speed = 0.1
scoreboard = Scoreboard()
player = Player()
screen.listen()
screen.onkey(player.move_player, "Up")
cars_list = []
for x in range(30):
    car = CarManager()
    cars_list.append(car)
print(cars_list)
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    for cars in cars_list:
        car_game = random.choice(cars_list)
        cars.move_forward()
        if cars.distance(-300, cars.ycor()) < 5:
            cars.off_screen_reset()

        if player.ycor() > 300:
            player.goto(0, -280)
            speed *= 0.8
            scoreboard.level_up()

        if cars.distance(player.player_position()) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()





