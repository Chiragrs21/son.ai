import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser as web
import pyautogui
from time import sleep
import os

# Your Spotify client credentials
client_id = '6728d84258c74d4ca71285565d4981e9'
client_secret = '762b832f9cae4e7b8c1073aa39182215'
count = 0

# Load the CSV file into a DataFrame
music_df = pd.read_csv('angry.csv')


for i in range(0, 10):
    new_list = []
    first_row = music_df.iloc[i].tolist()
    new_list.append(first_row)
    print(first_row)
    song_name = new_list[0][1]    # Assuming Name is the first column
    artist_name = new_list[0][3]  # Assuming Artist is the third column
# Authenticate with Spotipy

    sp = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

    # Search for the song using artist and track name
    result = sp.search(
        q=f"track:{song_name} artist:{artist_name}", type='track')

    # Check if search results contain matching tracks
    if result['tracks']['items']:
        # Get the first track from the search results
        track = result['tracks']['items'][0]
        count += 1

        def song_play():
            sleep(5)

        if (count == 1):
            song_play()
        # Extract the Spotify URI of the track
        track_uri = track['uri']
        web.open(track_uri)

        pyautogui.press('enter')

        print(f"Playing {song_name} by {artist_name}")

    else:
        print(f"Song not found: {song_name} by {artist_name}")
    sleep(20)
