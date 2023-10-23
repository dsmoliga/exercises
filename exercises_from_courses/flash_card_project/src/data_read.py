import pandas
import random


class DataRead():
    def __init__(self):
        self.data = pandas.read_csv(
            "flash_card_project\data\\french_words.csv")
        self.to_learn = self.data.to_dict(orient="records")
        self._lang_name = self.data.columns[0]

    @property
    def lang_name(self):
        return self._lang_name

    @lang_name.setter
    def lang_name(self, value):
        self._lang_name = self.data.columns[value]
        return self._lang_name

    def random_word(self):
        return random.choice(self.to_learn)
