from tkinter import PhotoImage, Button


class FlashyButton(Button):
    def __init__(self, button_img, button_col, button_row):
        self.my_image = PhotoImage(
            file=button_img)
        super().__init__(image=self.my_image, highlightthickness=0)
        self.grid(column=button_col, row=button_row)
