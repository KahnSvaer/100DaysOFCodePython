from turtle import Turtle
import time

STARTING_X = 3
STARTING_Y = 5
INITIAL_REFRESH = 0.05
Y_MAX_BALL = 200


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('sky blue')
        self.shapesize(.7)
        self.y_speed = STARTING_Y
        self.x_speed = STARTING_X
        self.refresh_speed = INITIAL_REFRESH

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

        if self.ycor() > Y_MAX_BALL or self.ycor() < -Y_MAX_BALL:
            self.y_speed *= -1

    def next(self):
        self.home()
        time.sleep(1)
        self.move()

    def bounce(self):
        self.x_speed *= -1
        self.refresh_speed *= 0.95
