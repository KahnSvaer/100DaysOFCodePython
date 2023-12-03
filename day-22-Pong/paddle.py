from turtle import Turtle

Y_MAX = 180
PADDLE = (0.6, 3)
SPEED = 15


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(PADDLE[0], PADDLE[1])
        self.speed('fastest')
        self.seth(90)
        self.home_position = position
        self.home()

    def home(self):
        self.goto(self.home_position)

    def up(self):
        if self.ycor() < Y_MAX:
            self.forward(SPEED)

    def down(self):
        if self.ycor() > -Y_MAX:
            self.backward(SPEED)
