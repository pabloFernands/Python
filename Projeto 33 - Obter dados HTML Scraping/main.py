import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_text = response.text

soup = BeautifulSoup(website_text, "html.parser")

articles = soup.find_all("h3", class_="title")

top_films = [movie.getText() for movie in articles]

# for films in articles:
#     name = films.getText()
#     top_films.append(name)

#print(top_films)

best_films = list(reversed(top_films))
#print(top_films)

movies = "movies.txt"

with open(movies, "w", encoding='utf-8') as file:
    for movies in best_films:
        file.write(movies + "\n")

