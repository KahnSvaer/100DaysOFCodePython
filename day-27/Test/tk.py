import tkinter as tk

window = tk.Tk()
window.title("Clicking Speed")
window.minsize(400, 400)

label = tk.Label(text="Welcome! Enter you name below and click to confirm")
label.pack()

name = tk.Entry()
name.pack()


def clicked():
    label["text"] = f"Welcome to the autoclicker, {name.get().capitalize()}! Click below to start"


button = tk.Button(text="Click me", command=clicked, height=25, width=60)
button.pack(expand=1)

window.mainloop()
