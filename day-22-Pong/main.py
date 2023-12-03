from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time

# Screen setup
screen = Screen()
screen.title("Pong")
screen.tracer(0)
screen.bgcolor('black')
screen.setup(800, 450)


INITIAL_REFRESH = 0.05
PADDLE_R_POSITION = (330, 0)
PADDLE_L_POSITION = (-330, 0)

# objects
paddle_R = Paddle(PADDLE_R_POSITION)
paddle_L = Paddle(PADDLE_L_POSITION)
scoreboard = ScoreBoard()
ball = Ball()

screen.update()


def game_stage_reset():
    ball.bounce()
    ball.refresh_speed = INITIAL_REFRESH
    ball.next()
    paddle_L.home()
    paddle_R.home()
    screen.update()
    time.sleep(1)


# Key Presses
screen.listen()
screen.onkeypress(key='Up', fun=paddle_R.up)
screen.onkeypress(key='w', fun=paddle_L.up)
screen.onkeypress(key='Down', fun=paddle_R.down)
screen.onkeypress(key='s', fun=paddle_L.down)


in_game = True
while in_game:
    ball.move()
    time.sleep(ball.refresh_speed)
    screen.update()

    # Scoring
    if ball.xcor() > 400:
        scoreboard.update(0)
        game_stage_reset()

    if ball.xcor() < -400:
        scoreboard.update(1)
        game_stage_reset()

    # Winning Conditions
    if scoreboard.score_L > 4:
        scoreboard.game_over(0)
        in_game = False

    if scoreboard.score_R > 4:
        scoreboard.game_over(1)
        in_game = False

    # Collisions with paddles
    if ((paddle_R.xcor() - ball.xcor()) < 16.0 and abs(paddle_R.ycor() - ball.ycor()) < 39.0
            and ball.x_speed > 0 and paddle_R.xcor() > ball.xcor()):
        ball.bounce()

    if ((ball.xcor() - paddle_L.xcor()) < 16.0 and abs(paddle_L.ycor() - ball.ycor()) < 39.0
            and ball.x_speed < 0 and ball.xcor() > paddle_L.xcor()):
        ball.bounce()


screen.exitonclick()
