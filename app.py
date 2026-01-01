from pyparsing import col
import streamlit as st
import pandas as pd
import pickle
import requests

def recommend(movie):
    l = []
    p = []
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])),reverse=True , key = lambda x : x[1])[1:6]
    for i in movie_list:
        l.append(movies.iloc[i[0]].title)
        p.append(fetch_poster(movies.iloc[i[0]].id))
    return l,p
    
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
    data = requests.get(url).json()

    if data.get('poster_path'):
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"


movies_dict = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommendation System")
selected_movies = st.selectbox("Select a Movie ", movies['title'].values)

if st.button("Recommend"):
    st.subheader("Movies you may like:")
    names , posters = recommend(selected_movies)
    print(names)
    print(posters)
    col= st.columns(len(names))
    for i in range(len(names)):
        with col[i]:
            st.header(names[i])
            st.image(posters[i])