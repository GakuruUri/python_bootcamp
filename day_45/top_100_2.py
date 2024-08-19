import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_time_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_names = [movie.getText() for movie in all_time_movies]

for n in range(len(movie_names)-1, -1, -1):
    pass

with open("Best_all_time_movies.txt", mode="w") as file:
    for movie in movie_names:
        file.write(f"{movie}\n")




# import requests
# from bs4 import BeautifulSoup

# URL = "https://www.empireonline.com/movies/features/best-movies-century/"

# response = requests.get(URL)
# website = response.text

# soup = BeautifulSoup(website, "html.parser")

# movie_list = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

# movie_titles = [movie.getText() for movie in movie_list]
# movies = movie_titles[::-1]

# with open("movies21century.txt", mode='w') as file:
#     for movie in movies:
#         file.write(f"{movie}\n")