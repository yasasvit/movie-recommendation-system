# Movie Recommendation System

This project is a movie recommendation system that uses a machine learning model to suggest 5 similar movies based on a chosen movie's title. The system is deployed using Heroku. It uses a pre-trained model and a similarity matrix to provide movie recommendations to users.

## Getting Started

To use this movie recommendation system, follow these steps:

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
2. Install the required dependencies using pip:

   ```sh
    pip install -r requirements.txt
3. Run the app.py file using Streamlit:

   ```sh
    streamlit run app.py
4. Access the application in your web browser at the provided URL

## Usage

1. Choose a movie from the provided dropdown menu or manually enter its name.

2. Click the "Recommend" button to get 5 movie recommendations based on your selection.

3. The recommendations will be displayed along with their posters if available.

## Files and Structure

- `app.py`: The main Streamlit application that powers the recommendation system.
- `movie_dict.pkl`: A pickled file containing movie data used by the application.
- `similarity.pkl`: A pickled file containing the similarity matrix for movie recommendations.
- `requirements.txt`: A list of required Python packages for the project.


