from turtle import Turtle, Screen

tut = Turtle()
tut.color("red")
for _ in range(10):
    tut.pendown()
    tut.forward(10)
    tut.penup()
    tut.forward(10)

screen = Screen()
screen.exitonclick()
