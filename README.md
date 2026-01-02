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

## Project Structure

- `app.py`: The main Streamlit application file containing the recommendation logic and UI.
- `main.ipynb`: Jupyter notebook used for data preprocessing, feature engineering, and model creation (generating `.pkl` files).
- `data/`: Directory containing the dataset (e.g., `tmdb_5000_movies.csv`).
- `movie.pkl`: Pickled Pandas DataFrame containing movie data (titles, IDs).
- `similarity.pkl`: Pickled cosine similarity matrix.

## Installation and Usage

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/subal43/DS-Movie-Recommended.git
    cd DS-Movie-Recommended
    ```
