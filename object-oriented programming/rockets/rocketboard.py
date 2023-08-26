from random import randint
from math import sqrt
from rocket import Rocket


class RocketBoard:
    def __init__(self, amount_of_rockets=5):
        self.rockets = [Rocket(randint(1, 6))
                        for _ in range(amount_of_rockets)]

        for _ in range(10):
            rocket_index_to_move = randint(0, len(self.rockets) - 1)
            self.rockets[rocket_index_to_move].move_up()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    def __len__(self):
        return len(self.rockets)

    @staticmethod
    def get_distance(rocket1, rocket2):
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2
        return sqrt(ab + bc)
