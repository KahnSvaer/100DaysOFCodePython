import colorgram
import turtle as t
from random import choice

colors = colorgram.extract('SpotPainting.jpeg', 50)
for i in range(len(colors)):
    colors[i] = colors[i].rgb.__getnewargs__()

colors = colors[4:]


def painting(dot_size, dot_distance, num_rows, num_columns, palette):
    turtle = t.Turtle()
    turtle.speed('fastest')
    turtle.hideturtle()
    t.colormode(255)
    turtle.penup()

    y_dist = (num_columns - 1) * dot_distance

    def paint_line(marker, size, dot_dist, num_dots, color_palette):
        x_dist = (num_dots - 1) * dot_dist
        marker.setx(-1 * x_dist / 2)
        for _ in range(num_dots):
            marker.dot(size, choice(color_palette))
            marker.forward(dot_dist)

    y = -1 * y_dist / 2
    for _ in range(num_columns):
        turtle.sety(y)
        y += dot_distance
        paint_line(turtle, dot_size, dot_distance, num_rows, palette)


painting(20, 50, 15, 15, colors)

screen = t.Screen()
screen.exitonclick()
