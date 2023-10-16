from tkinter import Canvas, PhotoImage
BACKGROUND_COLOR = "#B1DDC6"


class FlashyCard():
    def __init__(self):
        self.canvas = Canvas(width=800, height=526,
                             bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_front_image = PhotoImage(
            file=".\\flash_card_project\images\card_front.png")
        self.card_back_image = PhotoImage(
            file=".\\flash_card_project\images\card_back.png")
        self.card_background = self.canvas.create_image(
            400, 263, image=self.card_front_image)
        self.canvas.grid(column=0, row=0, columnspan=2)
        self.card_title = self.canvas.create_text(
            400, 150, font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(
            400, 263, font=("Ariel", 60, "bold"))
