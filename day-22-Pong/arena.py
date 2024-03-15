from turtle import Turtle

Y_BOUNDS = 280
DASH_SIZE = 30
FONT = ("avant-grande-medium", 30, "bold")


def arena_setup():
    turtle = Turtle()
    turtle.ht()
    turtle.speed("fastest")
    turtle.seth(90)
    turtle.color("white")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0, -Y_BOUNDS)
    while turtle.ycor() < Y_BOUNDS:
        turtle.pendown()
        turtle.forward(DASH_SIZE)
        turtle.penup()
        turtle.forward(DASH_SIZE)


def _update(turtle, score):
    turtle.clear()
    turtle.write(f"{score}", align="center", font=FONT)


class Arena:
    def __init__(self):
        self.enemy = Turtle()
        self.enemy_point = 0
        self.enemy.speed("fastest")
        self.enemy.color("white")
        self.enemy.goto(-30, 220)
        self.enemy.ht()
        _update(self.enemy, self.enemy_point)

        self.player = Turtle()
        self.player_point = 0
        self.player.speed("fastest")
        self.player.color("white")
        self.player.goto(30, 220)
        self.player.ht()
        _update(self.player, self.player_point)

    def enemy_(self):
        return self.enemy

    def player_(self):
        return self.player

    def add_score(self, is_player):
        if is_player:
            self.player_point += 1
            _update(self.player, self.player_point)

        else:
            self.enemy_point += 1
            _update(self.enemy, self.enemy_point)

    def game_over(self):
        self.player.home()
        self.player.write("Game Over.", align="center", font=FONT)
