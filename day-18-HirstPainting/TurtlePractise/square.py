from turtle import Turtle, Screen

marker = Turtle()
marker.color("blue3")
for i in range(4):
    marker.forward(100)
    marker.left(90)

screen = Screen()
screen.exitonclick()
