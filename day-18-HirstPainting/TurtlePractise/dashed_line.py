from turtle import Turtle, Screen

turtle_marker = Turtle()


def dashed_line(turtle, length, remaining=0, is_pen_up=False):
    def change_state(marker, is_up=True):
        if is_up:
            marker.pendown()
            return False
        else:
            marker.penup()
            return True

    if remaining:
        turtle.forward(remaining)
        is_pen_up = change_state(turtle, is_pen_up)

    while length > 5:
        turtle.forward(5)
        is_pen_up = change_state(turtle, is_pen_up)
        length -= 5

    turtle.forward(length)
    return is_pen_up


dashed_line(turtle_marker, length=305)
screen = Screen()
screen.exitonclick()
