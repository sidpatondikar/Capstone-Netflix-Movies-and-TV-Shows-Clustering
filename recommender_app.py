import streamlit as st
import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load the recommender data
def load_data():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    filepath_1 = os.path.join(current_directory, 'recommender files', 'final_data.csv')
    recommender_df = pd.read_csv(filepath_1)
    recommender_df.set_index('title', inplace=True)
    return recommender_df

# Calculate cosine similarity
def calculate_cosine_similarity(dataframe):
    CV = CountVectorizer()
    converted_matrix = CV.fit_transform(dataframe['text_data'])
    return cosine_similarity(converted_matrix)

# Recommend function
def recommend(title, cosine_sim, dataframe):
    try:
        recommend_content = []
        indices = pd.Series(dataframe.index)
        idx = indices[indices == title].index[0]
        series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
        top10 = list(series.iloc[1:11].index)

        for i in top10:
            recommend_content.append(list(dataframe.index)[i])
        
        recommended_movies = "\n- ".join(recommend_content)
        return f"If you like this '{title}', you may also enjoy:\n- {recommended_movies}"
    
    except:
        return "Please enter a valid name"

# Main Streamlit app
def main():
    st.title(':red[Netflix] Recommender System:tv:')
    st.markdown('<p style="color: white;">Content Data till 2019</p>', unsafe_allow_html=True)
    recommender_df = load_data()
    cosine_sim = calculate_cosine_similarity(recommender_df)

    # Dropdown for movie selection
    selected_movie = st.selectbox("Select a Show/Movie", recommender_df.index)
    
    # Recommend button
    if st.button("Recommend"):
        result = recommend(selected_movie, cosine_sim, recommender_df)
        st.subheader("Recommendations:")
        st.write(result)

if __name__ == "__main__":
    main()
