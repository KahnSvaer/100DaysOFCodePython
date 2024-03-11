from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear_screen():
    screen.resetscreen()


screen.onkeypress(fun=move_forward, key='Up')
screen.onkeypress(fun=move_backward, key='Down')
screen.onkeypress(fun=turn_left, key='Left')
screen.onkeypress(fun=turn_right, key='Right')
screen.onkeyrelease(fun=clear_screen, key='c')
screen.exitonclick()
