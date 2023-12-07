from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('cyan')
        self.penup()
        self.shapesize(.3)
        self.change_pos()

    def change_pos(self):
        random_x = randint(-14, 14) * 20
        random_y = randint(-14, 14) * 20
        self.speed('fastest')
        self.goto(x=random_x, y=random_y)
