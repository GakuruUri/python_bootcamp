from bs4 import BeautifulSoup
from pathlib import Path
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")


file_path = Path("100_movies.txt")
with file_path.open('w') as file:
    for file in response:
        100_movies.append(response)

