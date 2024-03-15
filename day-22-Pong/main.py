import time
from turtle import Screen
from arena import arena_setup, Arena
from paddle import PlayerPaddle, EnemyPaddle
from ball import Ball

RESET_TIME = 3
SCREEN_SIZE = [1000, 600]
BALL_BOUNCE_BOUNDARY = 458
AREA_LIMIT = 36
REFRESH_RATE = 0.01


def reset_and_score(is_player):
    arena.add_score(is_player)
    ball.reset()
    enemy.reset()
    player.reset()
    screen.update()
    time.sleep(1)


# Screen Setup
screen = Screen()
screen.setup(SCREEN_SIZE[0], SCREEN_SIZE[1])
screen.title("PONG!")
screen.bgcolor("black")
screen.tracer(0)

# Arena Setup
arena_setup()
arena = Arena()
enemy = EnemyPaddle()
player = PlayerPaddle()
ball = Ball()

# Controls
screen.listen()
screen.onkeypress(key="Up", fun=player.upward)
screen.onkeypress(key="Down", fun=player.downward)

# Game Loop
in_game = True
while in_game:
    time.sleep(REFRESH_RATE)
    screen.update()
    enemy.move()
    ball.move()

    # Scoring
    if ball.x_position() > SCREEN_SIZE[0] // 2:
        if arena.player_point > 5:
            arena.game_over()
            in_game = False
        else:
            reset_and_score(is_player=True)

    elif ball.x_position() < -SCREEN_SIZE[0] // 2:
        if arena.enemy_point > 5:
            arena.game_over()
            in_game = False
        else:
            reset_and_score(is_player=False)

    # Collision With paddles
    if (player.turtle.distance(ball.turtle) < 50 and
            player.turtle.xcor() > ball.x_position() > BALL_BOUNCE_BOUNDARY):
        ball.bounce()
    elif (enemy.turtle.distance(ball.turtle) < 50 and
          enemy.turtle.xcor() < ball.x_position() < -BALL_BOUNCE_BOUNDARY):
        ball.bounce()

    # Collision with wall done in ball logic only

screen.exitonclick()
