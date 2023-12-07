from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [[0, 0], [-20, 0], [-40, 0]]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.add_segment(STARTING_POSITIONS[i])
        self.head = self.segments[0]

    def add_segment(self, position):
        width, height = position
        turtle = Turtle('square')
        turtle.speed('fastest')
        turtle.color('white')
        turtle.penup()
        turtle.goto(width, height)
        self.segments.append(turtle)

    def go_top(self):
        if self.head.heading() in [0, 180]:
            self.head.seth(90)

    def go_bottom(self):
        if self.head.heading() in [0, 180]:
            self.head.seth(270)

    def go_left(self):
        if self.head.heading() in [90, 270]:
            self.head.seth(180)

    def go_right(self):
        if self.head.heading() in [90, 270]:
            self.head.seth(0)

    def move(self):
        self.segments[-1].goto(self.head.pos())
        self.head.forward(MOVE_DISTANCE)
        self.segments.insert(1, self.segments[-1])
        self.segments.pop()

    def reset(self):
        for segment in self.segments[::-1]:
            segment.ht()
        self.segments.clear()
        self.create_snake()
