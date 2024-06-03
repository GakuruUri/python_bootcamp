"""
1. Create screen.
2. Create and move a paddle.
3. Create another paddle.
4. Create another paddle.
5. Create the ball and make it move.
6. Detect collision with ball and bounce.
7. Detect collision with paddle.
8. Detect collision when paddle misses.
9. Keep score.
"""

from turtle import Screen, Turtle
import time

##TODO 1: Create screen.
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(390, 1)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()
