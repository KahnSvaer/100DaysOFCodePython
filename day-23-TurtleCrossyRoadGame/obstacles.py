import random
from turtle import Turtle

BLOCK_SIZE = (1.2, 2.4)
MAX_SPEED = 15
BOUNDARY = 290
LOWER_BOUNDARY = -220
UPPER_BOUNDARY = 250
MAX_SPAWN = 10


class Block(Turtle):
    def __init__(self):
        super().__init__('square')
        self.penup()
        self.x_speed = None
        self.random_abs_speed()
        self.random_color()
        self.shapesize(BLOCK_SIZE[0], BLOCK_SIZE[1])
        self.random_position()

    def random_color(self):
        r = random.random()
        g = random.random()
        b = random.random()
        color = (r, g, b)
        self.color('black', color)

    def random_abs_speed(self):
        self.x_speed = random.randint(5, 15)

    def random_position(self):
        y_position = random.randint(LOWER_BOUNDARY, UPPER_BOUNDARY)
        x_speed_sign = random.choice((-1, 1))
        self.goto(-1 * x_speed_sign * BOUNDARY, y_position)
        self.x_speed *= x_speed_sign

    def move(self):
        new_x_pos = self.xcor() + self.x_speed
        self.goto(new_x_pos, self.ycor())


class Obstacles:
    def __init__(self):
        self.obstacles = []
        self.start_level(1)

    def move(self):
        if len(self.obstacles):
            for block in self.obstacles:
                block.move()
        self.remove_outside()

    def spawner(self, level):
        if random.randint(0, MAX_SPAWN) < level:
            self.add_block()

    def add_block(self):
        new_block = Block()
        self.obstacles.append(new_block)

    def remove_block(self, block):
        block.ht()
        self.obstacles.remove(block)
        del block

    def remove_outside(self):
        for block in self.obstacles[::-1]:
            if block.xcor() > BOUNDARY + 50 or block.xcor() < -(BOUNDARY + 50):
                self.remove_block(block)

    def clear_screen(self):
        for block in self.obstacles[::-1]:
            self.remove_block(block)
        self.obstacles.clear()

    def start_level(self, level):
        for i in range(level * 3):
            self.add_block()
