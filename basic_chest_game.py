import random
from enum import Enum

def findApproximateValue(value, precentage):
    lowestValue = value - (precentage / 100) * value
    highestValue = value + (precentage / 100) * value
    return random.randint(lowestValue, highestValue)

Event = Enum('Event', ['Chest', 'Empty'])

eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                }

eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())

Colours = Enum('Colours', {'Green': 'green',
                           'Orange': 'orange',
                           'Purple': 'purple',
                           'Gold': 'gold'
                        }
            )

chestColoursDictionary = {
                            Colours.Green : 0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
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
        if (drawnEvent == Event.Chest):
            print("You've drawn a chest!")
            drawnChest = random.choices(chestColourList, chestColourProbability)[0]
            print("The chest colour is", drawnChest.value)
            gamerReward = findApproximateValue(rewardsForChests[drawnChest], 10)
            goldAcquired += gamerReward
        elif (drawnEvent == Event.Empty):
            print("You've got nothing, so unlucky!")
    else:
        print("You can go only further in this game :/ try again...")
        continue

    gameLenght -= 1

print("Congrats! You've acumulated", goldAcquired, "gold!")