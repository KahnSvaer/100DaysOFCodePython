import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
REFRESH_TIME = 1000

timer_start = False
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, timer_start
    timer_start = False
    if timer is not None:
        window.after_cancel(timer)
    reps = 1
    title_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="25:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global timer_start
    time = time_ui_manager(reps, timer_start)
    if not timer_start:
        timer_start = True
        timer_decrease(time)


def time_ui_manager(fn_reps, is_time_start):
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if fn_reps % 8 == 0:
        time = long_break_time
        title_label.config(text="Break", fg=RED)
        check_mark.config(text="")

    elif fn_reps % 2 == 0:
        time = short_break_time
        title_label.config(text="Break", fg=PINK)
        check_mark.config(text=CHECK_MARK * (fn_reps // 2))

    else:
        time = work_time
        title_label.config(text="Work", fg=GREEN)

    time_str = f"{time // 60:02.0f}:{time % 60:02.0f}"

    if not is_time_start:
        canvas.itemconfig(timer_text, text=time_str)

    return time


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_decrease(seconds):
    new_text = f"{seconds // 60:02.0f}:{seconds % 60:02.0f}"
    canvas.itemconfig(timer_text, text=new_text)
    if seconds:
        global timer
        timer = window.after(REFRESH_TIME, timer_decrease, seconds - 1)
    else:
        global reps, timer_start
        reps = (reps + 1) % 8
        timer_start = False
        time_ui_manager(reps, timer_start)


# --------------------------------- UI SETUP -------------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer!")
window.config(pady=60, padx=30, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="25:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

start_button = tk.Button(text="Start", width=10, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", width=10, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_mark = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "normal"))
check_mark.grid(column=1, row=3)

window.mainloop()
