from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray",
           "SeaGreen"]


# num_of_sides = 5

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shapes(shape_side_n)

screen = Screen()
screen.exitonclick()
