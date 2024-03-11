from turtle import Screen
from racer import Racer


COLORS_TABLE = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
INITIAL_XCOR = -230
DISTANCE_BETWEEN = 40

starting_ycor = DISTANCE_BETWEEN * (len(COLORS_TABLE) - 1) / 2

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="BET!!!", prompt="Who would win? Enter a color: ").strip().lower()

turtles = []

for i in range(len(COLORS_TABLE)):
    new_opponent = Racer(COLORS_TABLE[i], INITIAL_XCOR, starting_ycor - i * DISTANCE_BETWEEN)
    turtles.append(new_opponent)

win_color = ''
flag = False
while not flag:
    for racer in turtles:
        racer.move()
        if racer.is_finished():
            win_color = racer.color
            flag = True

if user_bet.lower() == win_color.lower():
    print(f"{win_color.capitalize()} wins the race. You WIN!")
else:
    print(f"{win_color.capitalize()} wins the race. You LOSE!")

screen.exitonclick()
