import requests
from bs4 import BeautifulSoup


date = input("Which year would you like to travel to? Type the date in thif format YYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/" + date

respose = requests.get(url)

soup = BeautifulSoup(respose.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)

#  id="title-of-a-story",

# response = requests.get(url)
# data = response.text

# soup = BeautifulSoup(data, "html.parser")
# section_heading = soup.find_all(name="h3", id="title-of-a-story")
# song_names = [song.getText().strip() for song in section_heading]

# print(song_names)