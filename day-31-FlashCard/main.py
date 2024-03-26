import tkinter as tk
from word_manager import DataManager

# -------------------- Constants ---------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
ANS_TIME = 3
# -------------------- UI Connector ---------------------- #
manager = DataManager()
invoker = None


def right_wrapper():
    next_word(True)


def wrong_wrapper():
    next_word(False)


def next_word(response=None):
    manager.word_change(correct_response=response)
    card = manager.card
    if card != {}:
        flip_card(card, is_front=True)
        global invoker
        if invoker is not None:
            # noinspection PyTypeChecker
            window.after_cancel(invoker)
        invoker = window.after(ANS_TIME*1000, flip_card, card, False)


def flip_card(card, is_front):
    if is_front:
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(word_text, text=card["French"].title(), fill="black")
        canvas.itemconfig(title_text, text="French", fill="black")
    else:
        canvas.itemconfig(canvas_image, image=back_image)
        canvas.itemconfig(word_text, text=card["English"].title(), fill="white")
        canvas.itemconfig(title_text, text="English", fill="white")


# -------------------- UI Setup ----------------------
window = tk.Tk()
window.title("Learn_With_Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = tk.PhotoImage(file="images/card_front.png")
back_image = tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

button_wrong_img = tk.PhotoImage(file="images/wrong.png")
button_wrong = tk.Button(image=button_wrong_img, highlightthickness=0, command=wrong_wrapper)
button_wrong.grid(column=0, row=1)

button_right_img = tk.PhotoImage(file="images/right.png")
button_right = tk.Button(image=button_right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=right_wrapper)
button_right.grid(column=1, row=1)

next_word()  # Starts the entire loop

window.mainloop()
