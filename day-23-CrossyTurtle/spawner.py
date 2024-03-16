import random
from math import copysign
from turtle import Turtle

X_BOUNDARY = 330
SPAWN_AREA = (-240, 260)
MAX_RATE = 1
MIN_RATE = 10


def _random_color():
    return random.random(), random.random(), random.random()


class _Block(Turtle):
    def __init__(self, level):
        super().__init__("square")
        self.shapesize(stretch_len=3)
        self.color(_random_color())
        self.penup()
        self.speed("fastest")
        self._initial_x = random.choice((-1, 1)) * X_BOUNDARY
        self._initial_y = random.randint(SPAWN_AREA[0], SPAWN_AREA[1])
        self.goto(self._initial_x, self._initial_y)
        self._x_speed = random.randint(3, 2 * level + 5)  # This should add enough randomness

    def move(self):
        self.forward(-1 * copysign(self._x_speed, self._initial_x))


class Spawner:
    def __init__(self):
        self.level = 1
        self.blocks = []
        self._spawn_level()

    def _spawn_level(self):
        for i in range(2 * self.level + 5):
            self.blocks.append(_Block(self.level))

    def next_level(self):
        self.level += 1
        for block in self.blocks:
            block.clear()
            block.ht()
        self.blocks.clear()
        self._spawn_level()
        return self.level

    def run(self):
        for block in self.blocks:
            block.move()
        if 1 == random.randint(1, self._random_spawn()):
            self.blocks.append(_Block(self.level))

    def _random_spawn(self):
        level_limit = MIN_RATE - self.level
        upper_limit = MAX_RATE
        return upper_limit if upper_limit > level_limit else level_limit
