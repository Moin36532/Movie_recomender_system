# import streamlit as st
# import pickle
# import pandas as pd
# import requests

# # =====================================
# # 🔧 1. Configuration
# # =====================================
# TMDB_API_KEY = "e1618ec42d475ad4f1cd9f369157548f"  # 🔑 replace this with your key
# import requests


# movies_df = pd.read_csv("movies_df.csv")
# movies_df["id"]
# import pickle
# import pandas as pd
# import streamlit as st


# movies_df = pd.read_csv("movies_df.csv")
# cosine_similarity = pickle.load(open("cosine_sim3.pkl",'rb'))
# indices = pd.Series(movies_df.index, index=movies_df["title_x"]).drop_duplicates()



# def get_recommendations(title, cosine_sim=cosine_similarity):
#     idx = indices[title]
#     similarity_scores = list(enumerate(cosine_sim[idx]))
#     similarity_scores= sorted(similarity_scores, key=lambda x: x[1], reverse=True)
#     similarity_scores= similarity_scores[1:9]
#     # (a, b) where a is id of movie, b is similarity_scores

#     movies_indices = [ind[0] for ind in similarity_scores]
#     movies = movies_df["title_x"].iloc[movies_indices]
#     movie_id = movies_df['id'].iloc[movies_indices]
#     return movies,movie_id


# get_recommendations("The Dark Knight Rises",cosine_similarity)



# # st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🎥", layout="centered")
# # st.title("🎬 Movie Recommender System")
# # st.markdown("##### Find movies similar to your favorites!")

# # ------------------------------
# # Movie Selection
# # ------------------------------
# # selected_movie = st.selectbox(
# #     "Select a movie you like 👇",
# #     movies_df["title_x"].values
# # )


# # if st.button("Show Recommendations 🎞️"):
# #     recommended_movies = get_recommendations(selected_movie,cosine_similarity)
# #     st.subheader("🎥 Top Recommendations:")
# #     for i, movie in enumerate(recommended_movies, start=1):
# #         st.write(f"**{i}.** {movie}")
import streamlit as st
st.image("https://image.tmdb.org/t/p/w500/aGuvNAaaZuWXYQQ6N2v7DeuP6mB.jpg",width= 180)

