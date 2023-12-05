from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from obstacles import Obstacles
import time

# Constants
REFRESH_SPEED = 0.1
WINNING_YCOR = 285

# Screen Setup
screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

# Objects
player = Player()
obstacles = Obstacles()
scoreboard = ScoreBoard()

screen.update()

# Screen Controls
screen.listen()
screen.onkey(key='Up', fun=player.move_up)
screen.onkey(key='w', fun=player.move_up)
screen.onkey(key='Left', fun=player.move_left)
screen.onkey(key='a', fun=player.move_left)
screen.onkey(key='Right', fun=player.move_right)
screen.onkey(key='d', fun=player.move_right)

# Main Loop
in_game = True

while in_game:
    obstacles.move()  # Controls the moving obstacles
    obstacles.spawner(scoreboard.level)  # Spawner
    time.sleep(REFRESH_SPEED)
    screen.update()

    # Collisions
    for block in obstacles.obstacles:
        if abs(block.xcor() - player.xcor()) < 36 and abs(block.ycor() - player.ycor()) < 24:
            scoreboard.game_over_popup()
            screen.update()
            in_game = False

    # Scoring and Winning Condition
    if player.ycor() > WINNING_YCOR:
        screen.update()
        if scoreboard.level > 5:
            scoreboard.win_popup()
            in_game = False
        else:
            scoreboard.next_level()
            obstacles.clear_screen()
            obstacles.start_level(scoreboard.level)
            player.home()
        scoreboard.update()



screen.exitonclick()
