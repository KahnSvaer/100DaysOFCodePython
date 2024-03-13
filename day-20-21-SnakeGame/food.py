import random
from turtle import Turtle

FOOD_COLOR = "blue"


class Food(Turtle):

    def __init__(self, x_size=600, y_size=600):
        super().__init__("square")
        self.color("blue")
        self.screen_size = (x_size // 40, y_size // 40)
        self.penup()
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        x_size, y_size = self.screen_size
        y_size -= 1
        x_size -= 1
        new_x_cor = random.randint(-1 * x_size, x_size)
        new_y_cor = random.randint(-1 * y_size, y_size)
        self.goto(new_x_cor * 20, new_y_cor * 20)
