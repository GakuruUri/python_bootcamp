from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward , "w")
screen.onkey(move_backwards , "s")
screen.onkey(turn_left , "a")
screen.onkey(turn_right , "d")
screen.onkey(clear, "c")
screen.exitonclick()




# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forward():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def move_left():
#     tim.left(10)
#
# def move_right():
#     tim.right(10)
#
# screen.listen()
# screen.onkey(key="d", fun=move_forward)
# screen.onkey(key="a", fun=move_backwards)
# screen.onkey(key="w", fun=move_left)
# screen.onkey(key="s", fun=move_right)
# screen.exitonclick()