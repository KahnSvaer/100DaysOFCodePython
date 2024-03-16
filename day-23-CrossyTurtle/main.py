import time
from turtle import Screen
from player import Player
from spawner import Spawner
from scoreboard import Scoreboard


def new_level():
    level = spawner.next_level()
    if level > 7:
        scoreboard.game_win()
        return False
    else:
        scoreboard.update_score()
        player.reset_position()
        return True


# Screen Setup
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.colormode(1)

# Objects Setup
player = Player()
spawner = Spawner()
scoreboard = Scoreboard()
screen.update()

# Controls
screen.listen()
screen.onkeypress(fun=player.move_up, key='Up')
screen.onkey(fun=player.move_left, key='Left')
screen.onkey(fun=player.move_right, key='Right')
screen.onkey(fun=new_level, key='l')

# Main Loop
in_game = True
while in_game:
    # Level Changer
    if player.turtle.ycor() > 300:
        in_game = new_level()

    # Main Runner
    spawner.run()

    # Detect Collisions
    for block in spawner.blocks:
        if player.turtle.distance(block) < 40 and 18 > player.turtle.ycor() - block.ycor() > -28:
            in_game = False
            scoreboard.game_over()

    # Updates
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
