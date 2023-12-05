from turtle import Turtle
import time

# Constants
LEVEL_POSITION = (-280, 265)
LEVEL_FONT = ('Courier', 15, 'bold')
GAME_OVER_FONT = ('Courier', 30, 'bold')
LEVEL_DELAY = 1


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.level = 0
        self.update()

    def update(self):
        self.goto(LEVEL_POSITION)
        self.level += 1
        self.clear()
        if self.level <= 5:
            self.write(arg=f'LEVEL: {self.level}', align='left', font=LEVEL_FONT)

    def game_over_popup(self):
        text = 'GAME OVER'
        self.goto(0, 0)
        self.write(text, font=GAME_OVER_FONT, align='center')

    def win_popup(self):
        text = 'YOU WIN'
        self.goto(0, 0)
        self.write(text, font=GAME_OVER_FONT, align='center')

    def next_level(self):
        text = 'LEVEL CROSSED'
        self.goto(0, 0)
        self.write(text, font=GAME_OVER_FONT, align='center')
        time.sleep(LEVEL_DELAY)
