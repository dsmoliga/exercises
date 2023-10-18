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
        self.cards.card_content(
            self.words_data.data.columns[0], self.current_card["French"], "black", self.cards.card_front_image)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def flip_card(self):
        self.cards.card_content(
            self.words_data.data.columns[1], self.current_card["English"], "white", self.cards.card_back_image)
