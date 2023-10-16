import pandas


class DataRead():
    def __init__(self):
        self.data = pandas.read_csv(
            "flash_card_project\data\\french_words.csv")
        self.to_learn = self.data.to_dict(orient="records")
