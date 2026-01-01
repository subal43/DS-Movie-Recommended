import streamlit as st
import pandas as pd
import pickle
import requests
import concurrent.futures

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])),reverse=True , key = lambda x : x[1])[1:6]
    
    recommended_movies = []
    recommended_movie_ids = []
    
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_ids.append(movies.iloc[i[0]].id)
    

    with concurrent.futures.ThreadPoolExecutor() as executor:
        recommended_posters = list(executor.map(fetch_poster, recommended_movie_ids))
        
    return recommended_movies, recommended_posters
    
@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        data = requests.get(url, timeout=5).json()
        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"
    except Exception:
        return "https://via.placeholder.com/300x450?text=Error"


with open('movie.pkl', 'rb') as f:
    movies_dict = pickle.load(f)
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

movies = pd.DataFrame(movies_dict)

st.title("Movie Recommendation System")
selected_movies = st.selectbox("Select a Movie ", movies['title'].values)

if st.button("Recommend"):
    st.subheader("Movies you may like:")
    names , posters = recommend(selected_movies)
    
    col= st.columns(len(names))
    for i in range(len(names)):
        with col[i]:
            st.text(names[i])
            st.image(posters[i])