import tkinter as tk

CONVERT_TO_KM = True

window = tk.Tk()
window.title("Units converter")
window.config(padx=20)

welcome_label = tk.Label(text="M->Km : Convertor", pady=10)
welcome_label.grid(column=1, row=0)

check_label = tk.Label(text="Miles:")
check_label.grid(column=0, row=1)

entry = tk.Entry(width=10)
entry.grid(column=2, row=1)

result_label = tk.Label(text="KiloMeters:")
result_label.grid(column=0, row=2)

calculated_label = tk.Label(text="0")
calculated_label.grid(column=2, row=2)


def calculate():
    text_input = entry.get().strip()
    if text_input.replace(".","").isdigit():
        result = float(entry.get().strip())
        result *= (1.60934 * CONVERT_TO_KM) + (0.621371 * (not CONVERT_TO_KM))
        calculated_label["text"] = round(result, 5)
        error["text"] = ""
    else:
        error["text"] = "ERROR!"


def reverse():
    global CONVERT_TO_KM
    CONVERT_TO_KM = not CONVERT_TO_KM
    if CONVERT_TO_KM:
        welcome_label.config(text="M->Km : Convertor")
        check_label.config(text="Miles:")
        result_label.config(text="KiloMeters:")
    else:
        welcome_label.config(text="Km->M : Convertor")
        check_label.config(text="KiloMeters:")
        result_label.config(text="Miles:")


change = tk.Button(text="<->", command=reverse)
change.grid(column=4, row=3)

button = tk.Button(text="Convert", command=calculate)
button.grid(column=1, row=3)

error = tk.Label(fg="red", pady=10)
error.grid(column=0, row=3)

window.mainloop()
