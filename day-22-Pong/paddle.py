from turtle import Turtle

PADDLE_POSITION = 470
PLAYER_MOVE_SPEED = 20
ENEMY_MOVE_SPEED = 4
BOUNDARY = (500, 280)
RESET_TIME = 3


class _Paddle:
    def __init__(self):
        self.turtle = Turtle("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.speed("fastest")
        self.turtle.seth(90)
        self.turtle.shapesize(stretch_len=3.4, stretch_wid=0.75)


class PlayerPaddle(_Paddle):

    def __init__(self):
        super().__init__()
        self.turtle.goto(PADDLE_POSITION, 0)

    def upward(self):
        if self.turtle.ycor() < BOUNDARY[1]:
            self.turtle.forward(PLAYER_MOVE_SPEED)

    def downward(self):
        if self.turtle.ycor() > -BOUNDARY[1]:
            self.turtle.backward(PLAYER_MOVE_SPEED)

    def reset(self):
        self.turtle.goto(PADDLE_POSITION, 0)


class EnemyPaddle(_Paddle):
    def __init__(self):
        super().__init__()
        self.turtle.goto(-PADDLE_POSITION, 0)
        self.direction = 1

    def move(self):
        self.turtle.forward(self.direction * ENEMY_MOVE_SPEED)
        if self.turtle.ycor() >= BOUNDARY[1]:
            self.direction *= -1
        elif self.turtle.ycor() <= -BOUNDARY[1]:
            self.direction *= -1

    def reset(self):
        self.turtle.goto(-PADDLE_POSITION, 0)
        self.direction = 1
        # Start Moving
