import streamlit as st
import pandas as pd
import pickle


def recommend(movie):
    l = []
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])),reverse=True , key = lambda x : x[1])[1:6]
    for i in movie_list :
        l.append(movies.iloc[i[0]].title)
    return l


movies_dict = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommendation System")
selected_movies = st.selectbox("Select a Movie ", movies['title'].values)
x =  recommend(selected_movies)


if st.button("Recommend"):
    st.subheader("Movies you may like:")
    for i in x:
        st.write(i)