from tkinter import Canvas, PhotoImage
BACKGROUND_COLOR = "#B1DDC6"


class FlashyCardSingleton():
    __instance = None

    @staticmethod
    def get_instance():
        if FlashyCardSingleton.__instance == None:
            FlashyCardSingleton("Default")
        return FlashyCardSingleton.__instance

    def __init__(self):
        if FlashyCardSingleton.__instance != None:
            raise Exception("You can only initialize this class once.")
        else:
            self.canvas = Canvas(width=800, height=526,
                                 bg=BACKGROUND_COLOR, highlightthickness=0)
            self._card_image = PhotoImage(
                file=".\\flash_card_project\images\card_front.png")
            self.card_background = self.canvas.create_image(
                400, 263, image=self.card_image)
            self.canvas.grid(column=0, row=0, columnspan=2)
            self.card_title = self.canvas.create_text(
                400, 150, font=("Ariel", 40, "italic"))
            self.card_word = self.canvas.create_text(
                400, 263, font=("Ariel", 60, "bold"))
            FlashyCardSingleton.__instance = self

    @property
    def card_image(self):
        return self._card_image

    @card_image.setter
    def card_image(self, side):
        self._card_image = PhotoImage(
            file=f".\\flash_card_project\images\{side}.png")
        return self._card_image

    def card_content(self, title, word, content_fill, card_side):
        self.canvas.itemconfig(
            self.card_title, text=title, fill=content_fill)
        self.canvas.itemconfig(
            self.card_word, text=word, fill=content_fill)
        self.canvas.itemconfig(self.card_background,
                               image=card_side)
