import streamlit as st
import pickle
import pandas as pd
import requests

# Load necessary data
m_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(m_list)
similarities = pickle.load(open('similarity.pkl', 'rb'))

# Format Streamlit host site
st.title('Movie Recommendation System')
selected_movie = st.selectbox('Please choose a movie from the provided dropdown menu or enter its name manually', movies['title'].values)

# Cache for optimization (not necessary) but increases efficiency if same title is selected multiple times
cached_images = {}

# Returns movie poster
def get_movie_image(title):
    if title in cached_images:
        return cached_images[title]
    
    api_key = "36b7480d"  
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    data = response.json()
    poster_url = data.get('Poster')

    if response.status_code == 200:
        if poster_url != 'N/A':
            cached_images[title] = poster_url
            return poster_url
    # else:
        # print("Error occurred while fetching movie poster:")
        # print(data) 
    return None

# Returns 5 closest recommendations to chosen movie
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarities[index]
    list_m = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    recommendations_images = []
    for m in list_m:
        recommendations.append(movies.iloc[m[0]].title)
        recommendations_images.append(get_movie_image(movies.iloc[m[0]].title))
    return recommendations, recommendations_images

if st.button('Recommend'):
    recommended_movies, images = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5): 
        if i < len(recommended_movies): 
            with cols[i]:
                st.text(recommended_movies[i])
                if images[i]:
                    st.image(images[i])
