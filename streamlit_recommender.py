import streamlit as st
import pandas as pd

# Set the page background color to black
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
        padding: 20px; /* Add padding to increase spacing between elements */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the Netflix logo centered
st.image("netflix_logo.png", width=200, caption="", use_column_width="always")

# Display the "Content Recommender" heading in Netflix red theme color, centered
st.markdown(
    """
    <h1 style="color: #E50914; text-align: center;">Content Recommender</h1>
    """,
    unsafe_allow_html=True,
)

# Create an input box for entering the movie or show name
movie_name = st.text_input(
    "Enter Movie/Show Here",  # Placeholder text
    "",  # Default value (empty string)
    key="movie_name_input",
    type="default",  # Type of input box
)

# Set the border color of the input box to Netflix red theme color
st.markdown(
    """
    <style>
    div[data-baseweb="input"] input {
        border: 2px solid #E50914;
        border-radius: 5px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add spacing between the input box and the button
st.write("")  # Add an empty line for spacing

# # Display recommendations based on the entered movie or show name (you'll need to implement this part)
# if st.button("Get Recommendations"):
#     # Call your recommender function here and display recommendations
#     recommendations = get_recommendations(movie_name)
#     st.subheader("Recommended Movies/Shows:")
#     for recommendation in recommendations:
#         st.write(recommendation)
