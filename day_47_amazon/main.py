from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/instant_pot/")
soup = BeautifulSoup(response.text, "html.parser")

pot_price = soup.find(name="span", class_="a-offscreen")
print(pot_price)