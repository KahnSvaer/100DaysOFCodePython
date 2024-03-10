import random
from turtle import Turtle, Screen
from colorgram import extract


def painting(turtle, color_list, radius, rows, columns):
    height = (radius * 2) * (rows - 1)
    width = (radius * 2) * (columns - 1)
    turtle.penup()
    turtle.sety(-1 * height / 2)
    turtle.setx(-1 * width / 2)
    turtle.seth(0)
    for j in range(rows):
        for k in range(columns):
            new_color = random.choice(color_list)
            turtle.dot(radius, new_color)
            turtle.forward(2 * radius)
        turtle.setx(-1 * width / 2)
        turtle.sety(turtle.ycor() + 2 * radius)
    turtle.ht()


colors = extract("Image.jpg", number_of_colors=20)[5:]
for i in range(len(colors)):
    colors[i] = list(colors[i].rgb)

turtle_pointer = Turtle()
screen = Screen()
screen.colormode(255)

painting(turtle_pointer, colors, 10, 11, 11)

screen.exitonclick()
