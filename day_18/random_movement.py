from turtle import Turtle, Screen
import random


jim = Turtle()
jim.color("red")
jim.shape("square")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]

for _ in range(200):
    jim.speed(100)
    jim.pensize(10)
    jim.color(random.choice(colours))
    jim.forward(30)
    jim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()