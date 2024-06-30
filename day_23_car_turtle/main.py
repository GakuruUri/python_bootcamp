"""
1. Move the turtle with keypress.
2. Create and move the cars.
3. Detect collision with car.
4. Detect when turtle reaches the other side.
5. Create a scoreboard.

"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

## TODO 1: Move the turtle with keypress.
player = Player()

## TODO 2. Create and move the cars.
car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

## TODO 3. Detect collision with car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

## TODO 4. Detect when turtle reaches the other side.
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()







screen.exitonclick()




