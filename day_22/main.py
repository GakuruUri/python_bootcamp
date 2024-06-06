"""
1. Create screen.
2. Create and move a paddle.
3. Create another paddle.
4. Create the ball and make it move.
5. Detect collision with ball and bounce.
6. Detect collision with paddle.
7. Detect collision when paddle misses.
8. Keep score.
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


##TODO 1: Create screen.
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)    # Turns off animation where the paddle is first drawn in the middle then moves to right



##TODO 3: Create another paddle.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

##TODO 4: Create the ball and make it move.
ball = Ball()
scoreboard = Scoreboard()

##TODO 2: Create and move a paddle.
# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(390, 0)
#
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Reactivates the paddle movement after paddle is created and animation stopped using tracer method.
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

##TODO 5: Detect collision with ball and bounce.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Need ball to bounce
        ball.bounce_y()


##TODO 6: Detect collision with paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


##TODO 7: Detect collision when paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
