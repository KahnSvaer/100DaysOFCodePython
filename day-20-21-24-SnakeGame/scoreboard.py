from turtle import Turtle

POSITION = (0, 265)
FONT = ('Courier', 18, 'bold')
FONT2 = ('Courier', 25, 'bold')


def get_high_score():
    with open("score.txt") as file:
        highscore = int(file.read().strip())
    return highscore


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('green')
        self.ht()
        self.penup()
        self.goto(POSITION)
        self.score = -1
        self.high_score = get_high_score()
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(arg=f'Score: {self.score}, HighScore: {self.high_score}', align='center', font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = -1
        self.update()


