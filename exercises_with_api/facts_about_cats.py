import requests
import json
import webbrowser
import pprint


### FIRST EXERCISE ###
"""params = {
    "amount": 5,
    "animal_type": "dog"
}

r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Wrong format!")
else:
    for cat in content:
        print(cat["text"])"""


### SECOND EXERCISE ###

"""params = {
    "breed_ids": "acur",
    "limit": 5
}

r = requests.get("https://api.thecatapi.com/v1/images/search", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Wrong format!")
else:
    for cat in content:
        webbrowser.open_new_tab(cat['url'])"""

### THIRD EXERCISE ###

params = {
    "api_key": "xkwS5Dj8nKXwnKtaMHGmsK0vrahc6hqK",
    "country": "pl",
    "year": 2023
}

r = requests.get("https://calendarific.com/api/v2/holidays", params)


try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Wrong format!")
else:
    pprint.pprint(content)