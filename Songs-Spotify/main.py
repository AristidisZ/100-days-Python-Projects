import requests
from bs4 import BeautifulSoup

from datetime import datetime
import sys

import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "948230b546844e8bba162ba0711b7795"
Client_SE = "c9eacca7bd7f4630a36d1163a195f7c9"



while True:
    travel_date = input('Year to travel too ? ')
    try:
        travel_date = datetime.strptime(travel_date, "%Y/%m/%d")
        break
    except ValueError:
        print("Error: must be format yyyy/mm/dd ")
        userkey = input("press 1 to try again or 0 to exit:")
        if userkey == "0":
            sys.exit()

print(f"travel_date is {travel_date.date()}")

url = f"https://www.billboard.com/charts/hot-100/{travel_date.date()}/"
# test_url = "https://www.billboard.com/charts/hot-100/2000-08-12/"

print(url)
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
songs_list = []
for song in songs:
    # print(song.getText().strip())
    songs_list.append(song.getText().strip())

print(songs_list)
body = {
    "grant_type": "client_credentials",
    "client_id": Client_ID,
    "client_secret": Client_SE,
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
#
spotify = requests.post(url="https://accounts.spotify.com/api/token",
                        headers=headers,
                        data=body)

tokens = spotify.json()
print(tokens)
access_token = tokens["access_token"]
# access_token = "BQAQ6BkO1JiGQP5ADsR3aYeV42o6BoUHSIFhJwo-XsqJg1VjP7s9Ieek5-sFMWFVw6aAqvvkgQNUOvbMlDmcbtAZTEqkK-Ap_3QioCsqyVHSNSA71Eo"
# print(access_token)

artist_url = "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb"

# Set headers as a dictionary
headers_token = {
    "Authorization": f"Bearer {access_token}"
}

# Make the GET request to the Spotify API
artist_response = requests.get(url=artist_url, headers=headers_token)

if artist_response.status_code == 200:
    artist_data = artist_response.json()
    # Now you can work with the artist data as needed
    # print(artist_data)
else:
    print(f"Error: {artist_response.status_code}, {artist_response.text}")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID,
                                               client_secret=Client_SE,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               )
                     )

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []

for song in songs_list:
    result = sp.search(q=f"track:{song}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id,
                        name=f"Top 100 {travel_date}",
                        public=False,
                        )

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
