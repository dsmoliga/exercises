import random
from enum import Enum

def findApproximateValue(value, precentage):
    lowestValue = value - (precentage / 100) * value
    highestValue = value + (precentage / 100) * value
    return random.randint(lowestValue, highestValue)

eventDictionary = {
                    "Chest": 0.6,
                    "Empty": 0.4
                }

eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())


chestColoursDictionary = {
                            "green" : 0.75,
                            "orange" : 0.2,
                            "purple" : 0.04,
                            "gold" : 0.01
                        }

chestColourList = tuple(chestColoursDictionary.keys())
chestColourProbability = tuple(chestColoursDictionary.values())

rewardsForChests = {
                        chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
                        for reward in range(len(chestColourList))
                        
                }

gameLenght = 5
goldAcquired = 0

print("Welcome to my game that rely on going straight!")


while gameLenght > 0:
    gameAnswer = input("Do you want to go straight?")
    if (gameAnswer == "yes"):
        print("Great, let's see what you got...")
        drawnEvent = random.choices(eventList, eventProbability)[0]
        if (drawnEvent == "Chest"):
            print("You've drawn a chest!")
            drawnChest = random.choices(chestColourList, chestColourProbability)[0]
            print(f"The chest colour is {drawnChest}...")
            gamerReward = findApproximateValue(rewardsForChests[drawnChest], 10)
            goldAcquired += gamerReward
        elif (drawnEvent == "Empty"):
            print("You've got nothing, so unlucky!")
    else:
        print("You can go only further in this game :/ try again...")
        continue

    gameLenght -= 1

print(f"Congrats! You've acumulated {goldAcquired} gold!")