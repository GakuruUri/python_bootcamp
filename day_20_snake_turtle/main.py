"""
1. Create a snake body
2. Move the snake
3. Detect Collision with food.
4. Create a scoreboard
5. Detect collision with wall
6. Detect collision with tail
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

## TODO 1: Create a snake body

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

## TODO 2: Move the snake
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
## TODO 3: Detect collision with food
    if snake.head.distance(food) < 15:
        #   print("nom nom nom")
        food.refresh()
        snake.extend()
## TODO 4: Create a scoreboard
        scoreboard.increase_score()

    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    #
    # segments[0].forward(20)
## TODO 5: Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()


## TODO 6: Detect collision with tail.
    # for segment in snake.segments[1:]:
    #     # if segment == snake.head:
    #     #     pass
    #
    #     # if head collides with any segment in the tail:
    #     if snake.head.distance(segment) < 10:
    #         # game_is_on = False
    #         scoreboard.game_over()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
