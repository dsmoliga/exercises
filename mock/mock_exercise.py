import requests
from random import randint


def get_elixir_id():
    url = f'https://wizard-world-api.herokuapp.com/Elixirs'
    response = requests.get(url)
    content = response.json()
    random_num = randint(0, 144)
    elixir_id = content[random_num]['id']

    return str(elixir_id)


def get_elixir(elixir_id):
    url = f'https://wizard-world-api.herokuapp.com/Elixirs/{elixir_id}'
    response = requests.get(url)
    my_elixir = response.json()
    return my_elixir['name']


my_id = get_elixir_id()
my_elixir = get_elixir(my_id)
print(my_elixir)
