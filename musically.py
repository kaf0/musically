import os
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify API client
client_id = os.environ["SPOTIFY_CLIENT_ID"]
client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# List of liked songs
liked_song_ids = [
    "song_id_1",
    "song_id_2",
    "song_id_3"
]

# Get features of liked songs
liked_songs_features = []
for song_id in liked_song_ids:
    features = sp.audio_features(song_id)[0]
    liked_songs_features.append(features)

# Create a DataFrame for liked songs
liked_songs_df = pd.DataFrame(liked_songs_features)

# Get a list of songs to compare
playlist_id = "playlist_id"  # Replace with a playlist ID containing songs to compare
results = sp.playlist_tracks(playlist_id)
tracks = results["items"]

# Get features for songs in the playlist
playlist_songs_features = []
for track in tracks:
    track_id = track["track"]["id"]
    features = sp.audio_features(track_id)[0]
    playlist_songs_features.append(features)

# Create a DataFrame for playlist songs
playlist_songs_df = pd.DataFrame(playlist_songs_features)

# Calculate similarity using cosine similarity
from sklearn.metrics.pairwise import cosine_similarity

similarity_matrix = cosine_similarity(liked_songs_df, playlist_songs_df)

# Recommend top N songs
N = 5
top_N_indices = similarity_matrix.mean(axis=0).argsort()[-N:][::-1]

recommended_songs = [tracks[i]["track"]["name"] for i in top_N_indices]
print("Recommended songs:", recommended_songs)
