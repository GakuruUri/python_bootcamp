from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)

# print(soup.prettify())

# print(soup.a, "\n") # find anchor tag
# print(soup.li, "\n")    # find list items
# print(soup.p, "\n") # Find a paragraph

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())  # get all plaintext
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)


section_heading = soup.find(name="h3", class_="heading")
print("----")
print(section_heading)
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)


name = soup.select_one(selector="#name")
print(name)


headings = soup.select(".heading")
print(headings)