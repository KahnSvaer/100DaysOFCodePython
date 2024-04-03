import tkinter as tk
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
WIN_COLOR = 'green'
LOSE_COLOR = 'red'

FONT = "Arial"
TIMER = 200


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.config(bg=THEME_COLOR, padx=30, pady=30)
        self.window.title("Quizzler")

        self.canvas = tk.Canvas(width=300, height=250)
        self.q_label = self.canvas.create_text(150, 125,
                                               text="Some question text",
                                               width=280,
                                               font=(FONT, 15, "italic"),
                                               fill=THEME_COLOR)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)

        self.score_label = tk.Label(text="Score: 0", font=(FONT, 12, "normal"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=1, column=1)

        yes_image = tk.PhotoImage(file='Images/true.png')
        self.yes_button = tk.Button(image=yes_image, highlightthickness=0, command=self.true_response)
        self.yes_button.grid(row=3, column=0)

        no_image = tk.PhotoImage(file='Images/false.png')
        self.no_button = tk.Button(image=no_image, highlightthickness=0, command=self.false_response)
        self.no_button.grid(row=3, column=1)

        self._get_next_question()

        self.window.mainloop()

    def _get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.q_label, text=question)
            self.yes_button.config(state='active')
            self.no_button.config(state='active')
        else:
            self.canvas.itemconfig(self.q_label, text="You've reached the end of the quiz")

    def _check_answer(self, response: bool):
        is_correct = self.quiz.check_answer(str(response))
        if is_correct:
            self.canvas.config(bg=WIN_COLOR)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg=LOSE_COLOR)
        self.yes_button.config(state='disabled')
        self.no_button.config(state='disabled')
        self.window.after(TIMER, self._get_next_question)

    def true_response(self):
        self._check_answer(True)

    def false_response(self):
        self._check_answer(False)
