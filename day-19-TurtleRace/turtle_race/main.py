from random import randint
from turtle import Turtle, Screen


def create_turtle(color):
    turtle = Turtle(shape='turtle' )
    turtle.color(color)
    turtle.penup()
    turtle.backward(230)
    return turtle


turtles = []
colors = ['indigo','blue','green','yellow','orange','red']
colors.reverse()
turtle_distance = 40
is_on = True

screen = Screen()
screen.setup(width=500,height=400)

y_pos = -1*turtle_distance*(len(colors)-1)/2

for num in range(len(colors)):
    turtle = create_turtle(colors[num])
    turtle.sety(y_pos)
    y_pos += turtle_distance
    turtles.append(turtle)


guess = screen.textinput(title="Make your bet", prompt='Which turtle will win the race? Enter the color:')

winner = 'red'
while is_on:
    for turtle in turtles:
        dist = randint(0,10)
        turtle.forward(dist)
        if turtle.xcor() >= 220:
            is_on = False
            winner = turtle
            break

if winner.pencolor().lower() == guess.lower():
    print("You have won! :)")
else:
    print("You have lost. :(")

print(f"The winner is: {winner.pencolor().capitalize()}")
screen.exitonclick()
