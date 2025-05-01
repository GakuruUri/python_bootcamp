import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.color("orange")
tim.shape("turtle")
turtle.colormode(255)

def rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color

for _ in range(1000):
    tim.color(rgb_color())
    tim.circle(100)
    tim.forward(1)
    tim.left(10)
    tim.speed(200)

screen = Screen()
screen.exitonclick()
