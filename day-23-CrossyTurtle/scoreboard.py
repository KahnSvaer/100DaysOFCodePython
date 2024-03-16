from turtle import Turtle

FONT = ("Courier", 20, "bold")
LOCATION = (-280, 260)


class Scoreboard:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.speed("fastest")
        self.turtle.ht()
        self.turtle.penup()
        self.turtle.goto(LOCATION)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.turtle.clear()
        self.level += 1
        self.turtle.write(f"Level {self.level}.", align="Left", font=FONT)

    def game_over(self):
        self.turtle.home()
        self.turtle.write(f"Game Over.", align="center", font=FONT)

    def game_win(self):
        self.turtle.home()
        self.turtle.write(f"You Win.", align="center", font=FONT)
