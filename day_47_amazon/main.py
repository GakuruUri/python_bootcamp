from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/instant_pot/")
soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
# print(price)

#Remove dollar sign using split
price_without_sign = price.split("$")[1]    # this is now a string
# print(price_without_sign) 


#Convert price without dollar sign into a float
price_as_float = float(price_without_sign)
print(price_as_float)