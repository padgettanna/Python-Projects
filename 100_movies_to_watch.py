import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")
titles = soup.find_all(name="h3", class_="title")
movies_list = []

for title in titles:
    movies_list.append(title.get_text())
    reversed_list = movies_list[::-1]
with open("movie_list.txt", "w") as file:
    for movie in reversed_list:
        file.writelines(movie+"\n")
