import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_done_tasks(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if entry["completed"] == True:
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1
    return completedTaskFrequencyByUser

def top_users(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedTasks = []
    maxAmountOfCompletedTasks = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTasks in completedTaskFrequencyByUser.items():
        if numberOfCompletedTasks == maxAmountOfCompletedTasks:
            usersIdWithMaxCompletedTasks.append(userId)
    return usersIdWithMaxCompletedTasks




try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format!")
else:
    completedTaskFrequencyByUser = count_done_tasks(tasks)
    usersIdWithMaxCompletedTasks = top_users(completedTaskFrequencyByUser)

print(f"The best users that done the most tasks are users: {usersIdWithMaxCompletedTasks}")



#first approach
"""
r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()

for user in users:
    if user["id"] in usersIdWithMaxCompletedTasks:
        print(f"Best user is {user['name']}")"""

#second approach
"""for userId in usersIdWithMaxCompletedTasks:
    r = requests.get("https://jsonplaceholder.typicode.com/users/" + str(userId))
    user = r.json()
    print(f"Best user is {user['name']}")"""

#third approach

def change_list_into_conj_of_param(my_list):
    conj_param = "id="
    
    lastItearation = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if i == lastItearation:
            conj_param += str(item)
        else:    
            conj_param += str(item) + "&id="

    return conj_param

conj_param = change_list_into_conj_of_param(usersIdWithMaxCompletedTasks)
r = requests.get("https://jsonplaceholder.typicode.com/users", params = conj_param)

users = r.json()

for user in users:
    print(f"Best user is {user['name']}")