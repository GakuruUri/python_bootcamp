from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# article_tag = soup.find(name="a", class_="storylink")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find_all(name="span", class_="score").getText()


# print(article_text)
# print(article_link)
# print(article_upvote)

articles = soup.find_all(name="a", class_="storylink")
article_text = []
article_links = []


article_tag = soup.find(name="a", class_="storylink")

for article_tag in articles:
    text = article_tag.getText()
    article_text.append(article_text)
    link = article_tag.get("href")
    article_links.append(article_link)


article_upvote = [score.getText() for score in soup.find_all(name="span", class_="score").getText()]


print(article_text)
print(article_link)
print(article_upvote)