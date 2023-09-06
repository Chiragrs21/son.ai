import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

auth_manager = SpotifyClientCredentials(
    '0c0027208e0e4483a506912762ef9dc1', '35e3ff108c7048b89f7a3bfce90b6cd1')
sp = spotipy.Spotify(auth_manager=auth_manager)


def getTrackIDs(user, playlist_id):
    track_ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        track_ids.append(track['id'])
    return track_ids


def getTrackFeatures(id):
    track_info = sp.track(id)

    name = track_info['name']
    album = track_info['album']['name']
    artist = track_info['album']['artists'][0]['name']
    # release_date = track_info['album']['release_date']
    # length = track_info['duration_ms']
    # popularity = track_info['popularity']

    track_data = [name, album, artist]  # , release_date, length, popularity
    return track_data

# Code for creating dataframe of feteched playlist


emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful",
                3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
music_dist = {0: "0IKVSSi9AB0Y2zr73EIXyG", 1: "0IKVSSi9AB0Y2zr73EIXyG", 2: "0NzAHfUg46ZQ8HsvfwPfWC",
              3: "2M7PPj4cpLXIxNcmPXrcG4", 4: "4PFwZ4h1LMAOwdwXqvSYHd", 5: "1MI8VpWOjBg7Jcv5CKensh", 6: "65CvVyeYPvZuZYqJcjpwA8"}

'''
Code can def be modularised into a function but i tried to write it when i was extremely sleepy so thought screw it and repeated code block

Uncomment for fetching updated playlists
'''


# track_ids = getTrackIDs('spotify', music_dist[0])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     # ,'Release_date','Length','Popularity'
#     df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist'])
#     df.to_csv('songs/angry.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify', music_dist[1])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     # ,'Release_date','Length','Popularity'
#     df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist'])
#     df.to_csv('songs/disgusted.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify', music_dist[2])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     # ,'Release_date','Length','Popularity'
#     df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist'])
#     df.to_csv('songs/fearful.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify', music_dist[3])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     # ,'Release_date','Length','Popularity'
#     df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist'])
#     df.to_csv('songs/happy.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify', music_dist[4])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     # ,'Release_date','Length','Popularity'
#     df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist'])
#     df.to_csv('songs/neutral.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify', music_dist[5])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     # ,'Release_date','Length','Popularity'
#     df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist'])
#     df.to_csv('songs/sad.csv')
# print("CSV Generated")

# track_ids = getTrackIDs('spotify', music_dist[6])
# track_list = []
# for i in range(len(track_ids)):
#     time.sleep(.3)
#     track_data = getTrackFeatures(track_ids[i])
#     track_list.append(track_data)
#     df = pd.DataFrame(track_list, columns=['Name', 'Album', 'Artist'])
#     df.to_csv('songs/surprised.csv')
# print("CSV Generated")
