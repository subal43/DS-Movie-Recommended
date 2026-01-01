# Movie Recommendation System

A content-based movie recommendation system built with Python and Streamlit. This application suggests movies similar to a user-selected movie using cosine similarity and fetches movie posters via the TMDB API.

## Features

- **Interactive UI**: Built with Streamlit for a smooth user experience.
- **Content-Based Filtering**: Recommendation engine uses cosine similarity on movie data.
- **Real-time Poster Fetching**: Fetches high-quality movie posters using the TMDB API.
- **Parallel Processing**: Optimized to fetch multiple movie posters simultaneously for fast performance.

## Tech Stack

- **Python**: Core language.
- **Streamlit**: Web framework for the interface.
- **Pandas**: Data manipulation and analysis.
- **Scikit-learn**: Used for calculating cosine similarity (in `main.ipynb`).
- **Requests**: For making HTTP calls to the TMDB API.