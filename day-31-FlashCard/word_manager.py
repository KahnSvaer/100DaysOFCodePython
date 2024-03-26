import pandas as pd
import random

import tkinter.messagebox as box

FILE = "data/french_words.csv"
FILE2 = "data/words_to_learn.csv"


def _data_parser():
    new_file = None
    try:
        new_file = pd.read_csv(FILE2)
    except FileNotFoundError:
        try:
            new_file = pd.read_csv(FILE)
        except FileNotFoundError:
            box.showinfo("OOPS", message="Main File Not Found")
    finally:
        if new_file is not None:
            words_list = new_file.to_dict(orient="records")
            return words_list
        else:
            return []


class DataManager:  # Backend
    def __init__(self):
        self.words_list = _data_parser()
        self.card = {}

    def _next_card(self):
        if len(self.words_list) == 0:
            self.card = {}
            if not len(self.words_list):
                box.showinfo(title="Hurray!", message="All words Learnt")
            return
        self.card = random.choice(self.words_list)

    def _remove_cur_card(self):
        self.words_list.remove(self.card)

    def _add_to_file(self):
        pd.DataFrame(self.words_list).to_csv(FILE2, index=False)

    def word_change(self, correct_response):
        if self.card != {}:
            if correct_response:
                self._remove_cur_card()
                self._add_to_file()
        self._next_card()
