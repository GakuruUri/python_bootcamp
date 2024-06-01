from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# segments = []
# for position in STARTING_POSITIONS:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     self.segments.append(new_segment)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        #   print("nom nom nom")
        food.refresh()
        scoreboard.increase_score()

    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    #
    # segments[0].forward(20)

screen.exitonclick()


"""
1. Create a snake body
2. Move the snake
3. Detect Collision with food.
4. Create a scoreboard
5. Detect collision with wall
6. Detect collision with tail
"""