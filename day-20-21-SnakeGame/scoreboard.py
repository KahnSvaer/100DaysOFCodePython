from turtle import Turtle

POSITION = (0, 260)
FONT_PROP = ("center", "Courier", 20, "bold")


class Scoreboard:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.color("white")
        self.turtle.ht()
        self.turtle.penup()
        self.turtle.goto(POSITION[0], POSITION[1])
        self.score = 0
        self._update_scoreboard()

    def add_score(self):
        self.turtle.clear()
        self.score += 1
        self._update_scoreboard()

    def _update_scoreboard(self):
        self.turtle.write(f"Score: {self.score}", align=FONT_PROP[0], font=FONT_PROP[1:])

    def game_over(self):
        self.turtle.home()
        self.turtle.write("GAME OVER.", align=FONT_PROP[0], font=FONT_PROP[1:])
