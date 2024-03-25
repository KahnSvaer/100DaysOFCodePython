import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
FILE = "Password_data.json"
DEFAULT_EMAIL = "Shivansh.pachnanda1@gmail.com"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tk.END)

    password_list = []

    password_list.extend([random.choice(LETTERS) for _ in range(random.randint(8, 10))])
    password_list.extend([random.choice(NUMBERS) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(SYMBOLS) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(tk.END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_in_file():
    website_str = web_entry.get().strip().title()
    web_entry.delete(0, tk.END)
    web_entry.focus()

    user_str = user_entry.get().strip()
    user_entry.delete(0, tk.END)
    user_entry.insert(tk.END, DEFAULT_EMAIL)

    password_str = password_entry.get().strip()
    password_entry.delete(0, tk.END)

    if not (len(user_str) and len(password_str) and len(website_str)):
        messagebox.showinfo(title="Oops!", message="Please don't leave any field empty")
        return

    is_ok = messagebox.askokcancel(title="Continue?", message=f"Website: {website_str}\n"
                                                              f"Email: {user_str}\n"
                                                              f"Password: {password_str}\n"
                                                              f"Continue?")
    if is_ok:
        try:
            new_json_entry = {website_str: {"user": user_str, "password": password_str}}
            data = new_json_entry
            with open(FILE) as file:
                data = json.load(file)
                data.update(new_json_entry)
        except FileNotFoundError:
            pass  # Basically do nothing for this specific error a finally resolves it itself
        except json.JSONDecodeError:
            pass  # Basically do nothing for this specific error a finally resolves it itself
        finally:
            with open(FILE, "w") as file:
                json.dump(data, file, indent=4)


def search_in_file():
    website_str = web_entry.get().strip().title()
    web_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    user_entry.insert(tk.END, DEFAULT_EMAIL)
    web_entry.focus()

    if not len(website_str):
        messagebox.showinfo(title="Oops!", message="Please don't leave field empty")
        return

    try:
        with open(FILE) as file:
            new_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="Data File Not Found")
    else:
        if website_str in new_data:
            query_result = new_data[website_str]
            messagebox.showinfo(title="Query!", message=f"Website: {website_str}\n"
                                                        f"Email: {query_result['user']}\n"
                                                        f"Password: {query_result['password']}")
        else:
            messagebox.showinfo(title="Oops!", message="No info related to site.")



# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(height=200, width=200)
canvas.grid(column=1, row=0)
lock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)

web_label = tk.Label(text="Website")
web_label.grid(column=0, row=1)

web_entry = tk.Entry(width=33)
web_entry.grid(column=1, row=1, columnspan=1)
web_entry.focus()

web_button = tk.Button(text="Search", width=15, command=search_in_file)
web_button.grid(column=2, row=1)

user_label = tk.Label(text="Email/Username")
user_label.grid(column=0, row=2)

user_entry = tk.Entry(width=52)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(tk.END, DEFAULT_EMAIL)

password_label = tk.Label(text="Password")
password_label.grid(column=0, row=3)

password_entry = tk.Entry(width=33)
password_entry.grid(column=1, row=3, columnspan=1)

password_button = tk.Button(text="Generate Password", width=15, command=generate_password)
password_button.grid(column=2, row=3)

add_button = tk.Button(width=44, text="Add", command=write_in_file)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
