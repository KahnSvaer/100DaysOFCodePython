from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_SPEED = 15
SIDE_SPEED = 10


class Player:
    def __init__(self):
        self.turtle = Turtle("turtle")
        self.turtle.penup()
        self.turtle.speed("fastest")
        self.reset_position()
        self.turtle.seth(90)

    def reset_position(self):
        self.turtle.goto(STARTING_POSITION)

    def move_up(self):
        self.turtle.forward(MOVE_SPEED)

    def move_left(self):
        new_x_position = self.turtle.xcor() - SIDE_SPEED
        new_y_position = self.turtle.ycor()
        self.turtle.goto(new_x_position, new_y_position)

    def move_right(self):
        new_x_position = self.turtle.xcor() + SIDE_SPEED
        new_y_position = self.turtle.ycor()
        self.turtle.goto(new_x_position, new_y_position)
