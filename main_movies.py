# =====================================
# 🎬 MOVIE RECOMMENDER APP
# =====================================
# Author: Your Name
# Description: A Streamlit-based movie recommendation system that
# suggests similar movies using cosine similarity and TMDB data.
# =====================================

# ---------- Imports ----------
import gc
import gdown
import pickle
import joblib
import os
import requests
import pandas as pd
import streamlit as st


# =====================================
# 🧹 MEMORY MANAGEMENT
# =====================================
# Delete old variables and force garbage collection to ensure a clean state
try:
    del my_data
except NameError:
    pass

gc.collect()


# =====================================
# 📂 DATA LOADING
# =====================================
# Load the main movies dataset
movies_df = pd.read_csv("movies_df.csv")

# Load precomputed cosine similarity matrix
# cosine_similarity = joblib.load("cosine_sim3.pkl")
# Load this pickle file using google drive link:

file_id = "13HuNCth6cbcLy3x-ECheCKpDPxx67IFR"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

if not os.path.exists("cosine_sim3.pkl"):
    gdown.download(url, "cosine_sim3.pkl", quiet=False)

with open("cosine_sim3.pkl", "rb") as f:
    cosine_similarity = pickle.load(f)


# Create a reverse lookup index (movie title → index)
indices = pd.Series(movies_df.index, index=movies_df["title_x"]).drop_duplicates()


# =====================================
# 🔧 API CONFIGURATION
# =====================================
# Replace this with your own TMDB API key
TMDB_API_KEY = "e1618ec42d475ad4f1cd9f369157548f"


# =====================================
# 🧠 RECOMMENDATION FUNCTION
# =====================================
def get_recommendations(title, cosine_sim=cosine_similarity):
    """
    Given a movie title, return top 8 similar movies with their metadata.

    Parameters:
        title (str): The title of the movie to find recommendations for.
        cosine_sim (ndarray): The cosine similarity matrix.

    Returns:
        movies (list): List of recommended movie titles.
        movie_id (list): List of movie IDs.
        movie_image_url (list): List of poster URLs.
        movie_homepage (list): List of TMDB homepage URLs.
    """
    # Get index of the selected movie
    idx = indices[title]

    # Calculate pairwise similarity scores
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Select top 8 similar movies (excluding itself)
    similarity_scores = similarity_scores[1:9]
    movie_indices = [i[0] for i in similarity_scores]

    # Retrieve metadata from dataset
    movies = movies_df["title_x"].iloc[movie_indices]
    movie_id = movies_df["id"].iloc[movie_indices]
    movie_homepage = movies_df["homepage"].iloc[movie_indices]

    # Fetch posters from TMDB API
    movie_image_url = []
    for mid in movie_id:
        url = f"https://api.themoviedb.org/3/movie/{mid}?api_key={TMDB_API_KEY}&language=en-US"
        response = requests.get(url)
        data = response.json()

        poster_path = data.get("poster_path")
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
        movie_image_url.append(poster_url)

    return movies, movie_id, movie_image_url, movie_homepage


# =====================================
# 🎨 STREAMLIT UI CONFIGURATION
# =====================================
st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎥",
    layout="centered"
)

st.title("🎬 Movie Recommender System")
st.markdown("##### Discover movies similar to your favorites!")


# =====================================
# 🎯 MOVIE SELECTION
# =====================================
selected_movie = st.selectbox(
    "Select a movie you like 👇",
    movies_df["title_x"].values
)


# =====================================
# 🚀 SHOW RECOMMENDATIONS
# =====================================
if st.button("Show Recommendations 🎞️"):
    # Get recommendations
    titles, ids, images, homepages = get_recommendations(selected_movie, cosine_similarity)

    st.subheader("🎥 Top Recommendations:")

    # ---- First Row (Movies 1–4) ----
    cols1 = st.columns(4, gap="medium")
    for col, (title, img, url) in zip(cols1, zip(titles[:4], images[:4], homepages[:4])):
        col.markdown(
            f"""
            <a href="{url}" target="_blank">
                <img src="{img}" width="180"><br>
            </a>
            <b>{title}</b>
            """,
            unsafe_allow_html=True
        )

    # ---- Second Row (Movies 5–8) ----
    cols2 = st.columns(4, gap="medium")
    for col, (title, img, url) in zip(cols2, zip(titles[4:8], images[4:8], homepages[4:8])):
        col.markdown(
            f"""
            <a href="{url}" target="_blank">
                <img src="{img}" width="180"><br>
            </a>
            <b>{title}</b>
            """,
            unsafe_allow_html=True
        )
