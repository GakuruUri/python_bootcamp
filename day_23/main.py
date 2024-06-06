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
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
