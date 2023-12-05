from turtle import Turtle

# Constants
HOME_POSITION = (0, -280)
PLAYER_SIZE = 1.2
SIDE_SPEED = 20
FORWARD_SPEED = 15


class Player(Turtle):
    def __init__(self):
        super().__init__('turtle')
        self.penup()
        self.seth(90)
        self.shapesize(PLAYER_SIZE)
        self.home()

    def move_up(self):
        self.forward(FORWARD_SPEED)

    def move_left(self):
        new_x = self.xcor()
        if self.xcor() > -280:
            new_x -= SIDE_SPEED
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor()
        if self.xcor() < 280:
            new_x += SIDE_SPEED
        self.goto(new_x, self.ycor())

    def home(self):
        self.goto(HOME_POSITION)
