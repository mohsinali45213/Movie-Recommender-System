import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch poster from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)
    data = response.json()
    
    if 'poster_path' not in data or data['poster_path'] is None:
        # Return placeholder image if no poster available
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"
    
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

# Function to recommend movies
def recommended(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommended_movies = sorted(
        list(enumerate(distances)), key=lambda x: x[1], reverse=True
    )[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in recommended_movies:
        movie_id = movies.iloc[i[0]]['movie_id'] 
        recommended_movie_names.append(movies.iloc[i[0]]['title'])
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

# Load data
similarity = pickle.load(open('../models/similarity.pkl', 'rb'))
movie_dict = pickle.load(open('../models/movies.pkl', 'rb'))
movies = pd.DataFrame.from_dict(movie_dict)

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommended(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
