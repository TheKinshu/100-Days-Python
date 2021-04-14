#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import lxml

with open("./Day45/website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())


company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name.getText())

headings = soup.select(".heading")
print(headings)