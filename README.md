<center> <h1>Music Recommender Script Documentation</h1> </center>

<center> <h2>Overview</h2> </center>

This script provides a simple music recommender system based on a set of 'liked' songs. The recommender uses the Spotify Web API to fetch audio features for both the 'liked' songs and a given playlist. It then calculates the similarity between the 'liked' songs and the songs in the playlist using cosine similarity and recommends the top N most similar songs.

<center> <h2>Requirements</h2> </center>

    Python 3.6 or higher
    spotipy
    pandas
    A Spotify Developer account with a registered application (Client ID and Client Secret)


<center> <h2>Installation</h2> </center>

Install the required packages using pip:

pip install spotipy pandas

<center> <h2>Configuration</h2> </center>

    Register your application on the Spotify Developer Dashboard to get your Client ID and Client Secret.
    Set up environment variables for SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET with your actual Client ID and Client Secret.

<center> <h2>Usage</h2> </center>

    Replace the placeholders song_id_1, song_id_2, song_id_3, and playlist_id in the musically.py script with actual Spotify song IDs (for the 'liked' songs) and a playlist ID containing songs to compare.

    Set the number of recommended songs by changing the value of N.

    Run the Python script:

python musically.py

The script will output the top N recommended songs based on the similarity to the 'liked' songs.

<center> <h2>Customization</h2> </center>

    To use a different similarity metric, replace the cosine_similarity function with another similarity function from sklearn.metrics.pairwise (e.g., euclidean_distances or manhattan_distances).

    To filter the recommended songs by additional criteria, modify the recommended_songs list comprehension. For example, you can filter by a specific genre, popularity threshold, or release year.

    To further improve the recommender system, consider incorporating additional features such as song lyrics, genre information, or collaborative filtering based on user preferences.
