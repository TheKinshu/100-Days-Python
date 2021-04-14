import requests, lxml, spotipy
from pprint import pprint
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


URL = "https://www.billboard.com/charts/hot-100/"

CLIENT_ID = "Client_Id"
SECRET = "Secert"

REDIRECT_URL = "http://example.com/callback/"

#inputDate = input("Which year do you want to travel to? Type the date in this formate YYYY-MM-DD: ")
inputDate = "2000-08-15"
response = requests.get(f"{URL}" + inputDate)

website_html = response.text

soup = BeautifulSoup(website_html, "lxml")

content_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
content_artist = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")

songs = [song.getText() for song in content_songs]
artists = [artist.getText() for artist in content_artist]

date = inputDate.split("-")

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=SECRET,show_dialog=True, redirect_uri=REDIRECT_URL, scope=scope))

userID = sp.current_user()["id"]


songURI = [sp.search(f"artist:{artists[index]} {songs[index]}", limit=1) for index in range(len(songs))]

songs = [song["tracks"]["items"] for song in songURI if not song == []]

songID = [song[0]["uri"] for song in songs if not song  == []]

playlist = sp.user_playlist_create(user=userID,name=f"{inputDate} Billboard 100", public=False)

pprint(playlist["id"])

test = sp.playlist_add_items(playlist_id=playlist["id"],items=songID)

print(test)