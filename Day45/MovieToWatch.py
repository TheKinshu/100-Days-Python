from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

content = soup.find(name="div", class_="jsx-3821216435 block-item listicle-container")

movies = content.find_all(name='a')

reviewsMovies = [movie.getText() for movie in movies if "Read Empire's" in (movie.getText())]

movieList = []

for movie in reviewsMovies:
    temp = movie.split()
    movieList.append(' '.join(temp[4:]))

movieL = (movieList[::-1])

with open("./Day45/movie.txt", "w") as file:
    for movie in movieL:
        file.write(f"{movie}\n")