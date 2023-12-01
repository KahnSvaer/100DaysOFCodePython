from turtle import Turtle, Screen

turtle = Turtle()


def move_forward():
    turtle.forward(5)


def move_backward():
    turtle.backward(5)


def left():
    turtle.left(3)


def right():
    turtle.right(3)


def clear():
    screen.resetscreen()


screen = Screen()
screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=left)
screen.onkeypress(key='d', fun=right)
screen.onkeypress(key='c', fun=clear)
screen.exitonclick()
