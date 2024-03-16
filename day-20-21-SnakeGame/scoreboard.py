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
        self.highscore = self._find_highscore()
        self._update_scoreboard()

    def add_score(self):
        self.turtle.clear()
        self.score += 1
        self._update_scoreboard()

    def _update_scoreboard(self):
        self.turtle.write(f"Score: {self.score}, High_score: {self.highscore}", align=FONT_PROP[0], font=FONT_PROP[1:])

    def game_over(self):
        self.turtle.home()
        self.turtle.write("GAME OVER.", align=FONT_PROP[0], font=FONT_PROP[1:])

        # File Writer
        if self.score > self.highscore:
            with open("Highscore.txt", "w") as file:
                file.write(str(self.score))

    @staticmethod
    def _find_highscore():
        highscore = 0
        try:
            with open("Highscore.txt") as file:
                highscore = int(file.read().strip())
        except FileNotFoundError:
            pass
        return highscore
