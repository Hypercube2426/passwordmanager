import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# client_id = "e20d7fad60c1472995e26d1b93504db4"
# client_secret = "83b27564fb8946c58ef90ee5056a7ddd"
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

html = response.text
soup = BeautifulSoup(html, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="e20d7fad60c1472995e26d1b93504db4",
        client_secret="83b27564fb8946c58ef90ee5056a7ddd",
        show_dialog=True,
        cache_path="token.txt",
        username="eghgwu32ystmcitp05yt8lz3e",
    )
)
user_id = sp.current_user()["id"]
print(user_id)
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
