from tkinter import Tk
BACKGROUND_COLOR = "#B1DDC6"


class Screen(Tk):
    def __init__(self):
        super().__init__()
        self.title("Flashy")
        self.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
