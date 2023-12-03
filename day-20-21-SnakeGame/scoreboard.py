from turtle import Turtle

POSITION = (0, 265)
FONT = ('Courier', 18, 'bold')
FONT2 = ('Courier', 25, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('green')
        self.ht()
        self.penup()
        self.goto(POSITION)
        self.score = -1
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(arg=f'Score: {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT2, align='center')
