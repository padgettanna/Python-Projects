from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year would you like to travel to? Type the date in this format: YYYY-MM-DD: ")
year = date.split("-")[0]
URL = f"https://www.billboard.com/charts/hot-100/" + date
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret_code"
AUTH_URL= 'https://accounts.spotify.com/api/token'

response = requests.get(URL)
bilboard_web_page = response.text
songs_titles = []
song_uris = []

soup = BeautifulSoup(bilboard_web_page, "html.parser")
songs = soup.find_all(name="h3", class_="a-no-trucate")
for song in songs:
    songs_titles.append(song.get_text().strip())

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

for song in songs_titles:
    result = sp.search(q=f"track:{song}, year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_only = uri.split(":")[2]
        song_uris.append(uri_only)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
playlist_tracks = sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
