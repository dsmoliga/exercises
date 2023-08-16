import random


class Rocket:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def fly(self):
        flyActions = ['Fly', 'Stay']
        moveList = []
        for move in range(10):
            move = random.choices(flyActions, [50, 50])
            moveList.append(move)
        flyList = moveList.count(['Fly'])
        print(f'Rocket number {self.name} has flown {flyList} times out of 10 tries. Speed factor for this rocket is {self.speed}. Total distance this rocket has flown is {flyList * self.speed}')


rocketList = [
    Rocket(x, speed=random.randrange(5))
    for x in range(1, 6)
]

for y in range(5):
    rocketList[y].fly()
