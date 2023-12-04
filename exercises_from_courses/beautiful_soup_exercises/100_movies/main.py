import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

request = requests.get(URL)
source = request.text

soup = BeautifulSoup(source, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movies_list = [movie.getText() for movie in movies]
movies_list.reverse()

with open(file="best_movies.txt", mode="w", encoding="UTF-8") as file:
    for movie in movies_list:
        file.write(movie + "\n")
