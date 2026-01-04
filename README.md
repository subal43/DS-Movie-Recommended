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

2.  **Install Dependencies**

    Ensure you have Python installed. Install the required libraries:

    ```bash
    pip install streamlit pandas requests scikit-learn
    ```


3.  **Run the Application**

    ```bash
    streamlit run app.py
    ```
4.  **View the App**

    The app will open in your browser automatically. If not, navigate to `http://localhost:8501`.

## How It Works

1.  The system loads the pre-computed `movie_dict` and `similarity` matrix.
2.  When a user selects a movie, the app finds its index in the dataset.
3.  It looks up the similarity scores for that movie and identifies the top 5 most similar movies.
4.  The app uses the TMDB API to fetch posters for these recommendations.
5.  Results are displayed in a responsive grid layout.


## Data Source

The dataset used for this project is likely the TMDB 5000 Movie Dataset, which includes metadata on thousands of movies.

## License

This project is licensed under the MIT License.
