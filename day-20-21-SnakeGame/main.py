from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

REFRESH_RATE = 0.1

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake 2D")
screen.tracer(0)

snake = Snake()
scoreboard = ScoreBoard()
food = Food()

game_is_on = True
while game_is_on:
    snake.move()
    time.sleep(REFRESH_RATE)
    screen.update()

    screen.onkey(key='w', fun=snake.go_top)
    screen.onkey(key='s', fun=snake.go_bottom)
    screen.onkey(key='a', fun=snake.go_left)
    screen.onkey(key='d', fun=snake.go_right)

    if snake.head.distance(food) < 15:
        food.change_pos()
        scoreboard.update()
        snake.add_segment(snake.segments[-1].pos())

    if ((snake.head.xcor() > 280) or (snake.head.xcor() < -280)
            or (snake.head.ycor() > 280) or (snake.head.ycor() < -280)):
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
