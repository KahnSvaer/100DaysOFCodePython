import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

REFRESH_RATE = 0.1
PLAYER_BOUNDARY = (280, 280)

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()
food = Food()

screen.update()

screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")

in_game = True

while in_game:
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.relocate()
        scoreboard.add_score()
        snake.add_segment()

    # Detect Collision with wall
    if (snake.head.xcor() > PLAYER_BOUNDARY[0] or snake.head.xcor() < -PLAYER_BOUNDARY[0] or
            snake.head.ycor() > PLAYER_BOUNDARY[1] or snake.head.ycor() < -PLAYER_BOUNDARY[1]):
        in_game = False
        scoreboard.game_over()

    # Detect Collisions with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment)<15:
            in_game = False
            scoreboard.game_over()

    screen.update()
    time.sleep(REFRESH_RATE)

screen.exitonclick()
