from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

title = soup.title

articles = soup.find_all(name='a', class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    link =  article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]


# print(article_texts)
# print(article_links)
print(article_upvotes)

number = max(article_upvotes)

index = article_upvotes.index(number)
print(index)

print(article_texts[index+1])
print(article_links[index+1])
