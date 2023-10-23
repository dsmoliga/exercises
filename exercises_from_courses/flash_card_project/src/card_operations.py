from src.flashy_card import FlashyCardSingleton
from src.screen import Screen
from src.data_read import DataRead


class CardOperations():
    def __init__(self):
        self.window = Screen()
        self.cards = FlashyCardSingleton()
        self.words_data = DataRead()
        self.flip_timer = self.window.after(3000, func=self.flip_card)
        self.next_card()

    def next_card(self):
        self.words_data.lang_name = 0
        self.cards.card_image = "card_front"
        self.window.after_cancel(self.flip_timer)
        self.current_word = self.words_data.random_word()
        self.cards.card_content(
            self.words_data.lang_name, self.current_word[self.words_data.lang_name], "black", self.cards.card_image)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def flip_card(self):
        self.words_data.lang_name = 1
        self.cards.card_image = "card_back"
        self.cards.card_content(
            self.words_data.lang_name, self.current_word[self.words_data.lang_name], "white", self.cards.card_image)
