from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, initial_size=3):
        self.snake_body = []
        self.head = None  # Defining before as used in _create snake
        self._create_snake(initial_size)
        self.head = self.snake_body[0]
        self.head.color("skyblue")

    def _create_snake(self, initial_size):
        for i in range(initial_size):
            self.add_segment()

    def move(self):
        self.snake_body[-1].goto(self.head.position())
        last_segment = self.snake_body.pop()
        self.snake_body.insert(1, last_segment)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(-90)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)

    def add_segment(self):
        segment = Turtle("square")
        segment.color("white")
        segment.speed("fastest")
        segment.penup()
        if self.head is not None:
            segment.goto(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())
        self.snake_body.append(segment)
