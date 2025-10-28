🎬 Movie Recommender System

Hi! I created this Movie Recommender System, where you can find movies similar to the ones you like.
Just search for a movie (note: the latest releases might not be available) and get personalized recommendations instantly.

🧩 Libraries Used

Pandas

Streamlit

Scikit-learn (sklearn)

Requests

Pickle (Python built-in module)

💡 Features

If you find a movie interesting from the recommendations, simply click on its image — it will take you directly to the movie’s website for more details.
I’ll be adding more features soon to make the experience even better!

This is one of my Data Science projects. While recommender systems are quite common in the data science field, foundational projects like this one are great additions to your project portfolio, especially when combined with more advanced ones.

⚙️ How to Run This Repository

Here’s a quick description of the included files:

File	Description
Main_movies.py	The main file containing the core logic of the project.
film.py	A copy of the recommendation function from the main file — useful for debugging.
movies_df.csv	The processed dataset used in the project.
indices.csv	Contains the index mapping for locating specific movies.
similarity_pkl%20file.txt	A text file containing a Google Drive link to the pickle file of the cosine similarity matrix (too large to upload directly).
Movie_recommender_system.ipynb	Jupyter Notebook used to create the processed dataset and similarity pickle file.
requirements.txt	Contains all necessary dependencies — just install them, and you’re good to go!
🚀 Future Improvements

I plan to:

Add more datasets for newer movies

Improve recommendation accuracy

Enhance the user interface


git clone https://github.com/Moin36532/Movie_recomender_system.git
pip install -r requirements.txt
Enjoy!
