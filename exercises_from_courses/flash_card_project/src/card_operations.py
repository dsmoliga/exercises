from src.flashy_card import FlashyCard
from src.screen import Screen
from src.data_read import DataRead
import random


class CardOperations():
    def __init__(self):
        self.window = Screen()
        self.cards = FlashyCard()
        self.words_data = DataRead()
        self.flip_timer = self.window.after(3000, func=self.flip_card)
        self.next_card()

    def next_card(self):
        self.window.after_cancel(self.flip_timer)
        self.current_card = random.choice(self.words_data.to_learn)
        self.cards.canvas.itemconfig(
            self.cards.card_title, text="French", fill="black")
        self.cards.canvas.itemconfig(
            self.cards.card_word, text=self.current_card["French"], fill="black")
        self.cards.canvas.itemconfig(self.cards.card_background,
                                     image=self.cards.card_front_image)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def flip_card(self):
        self.cards.canvas.itemconfig(
            self.cards.card_title, text="English", fill="white")
        self.cards.canvas.itemconfig(
            self.cards.card_word, text=self.current_card["English"], fill="white")
        self.cards.canvas.itemconfig(self.cards.card_background,
                                     image=self.cards.card_back_image)
