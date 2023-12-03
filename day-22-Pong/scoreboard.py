from turtle import Turtle

POSITION = (0, 160)
FONT = ('Courier', 30, 'bold')
FONT2 = ('Courier', 50, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('green')
        self.ht()
        self.penup()
        self.goto(POSITION)
        self.score_L = 0
        self.score_R = 0
        self.update(2)

    def update(self, val):
        if val == 0:
            self.score_L += 1
        elif val == 1:
            self.score_R += 1

        self.clear()
        self.write(arg=f'{self.score_L} : {self.score_R}', align='center', font=FONT)

    def game_over(self, val):
        if val == 0:
            text = "LEFT WINS"
        else:
            text = "RIGHT WINS"
        self.goto(0, 0)
        self.write(text, font=FONT2, align='center')
