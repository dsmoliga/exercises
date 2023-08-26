class Rocket:
    id_of_rocket = 1

    def __init__(self, speed=1):
        self.altitude = 0
        self.speed = speed
        self.x = 0
        self.id = self.id_of_rocket
        Rocket.id_of_rocket += 1

    def move_up(self):
        self.altitude += self.speed

    def __str__(self) -> str:
        return f"Rocket no. {self.id} achieved {str(self.altitude)} height."
