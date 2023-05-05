Research & Project approval (Part 1)

Creating a music recommender based on a set of 'liked' songs involves several steps. Here's a high-level overview of how to approach this:

 1. Data collection:
    Collect a dataset of songs, including features like tempo, key, duration, danceability, energy, etc. You can use APIs like Spotify Web API or other music databases to gather this information.

 2. Data preprocessing:
    Clean the data by handling missing values, normalizing features, and converting categorical variables into numerical values.

 3. Feature selection:
    Choose relevant features that can help determine song similarity, such as genre, tempo, key, energy, danceability, etc.

 4. User preferences:
    Maintain a list of 'liked' songs for each user. These songs will be used to find similar songs and make recommendations.

 5. Calculate similarity:
    Calculate the similarity between the 'liked' songs and the other songs in the dataset using a similarity metric like cosine similarity, Euclidean distance, or Pearson correlation.

 6. Recommend songs:
    Sort the songs based on their similarity scores and recommend the top N songs to the user.
