# import turtle
#
# timmy = turtle.Turtle()
import turtle
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")

timmy.color('red')
timmy.forward(100)
timmy.left(90)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight, my_screen.canvwidth)
turtle.exitonclick()



my_screen = Screen()
print(my_screen.canvheight, my_screen.canvwidth)
my_screen.exitonclick()




