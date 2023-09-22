# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:36:59 2023

@author: sidpa
"""

import streamlit as st
import pandas as pd

# Set the page background color to black
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
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
    "Enter Movie/Show Here",
    "Type the name of a movie or show...",
    key="movie_name_input",
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

# Display recommendations based on the entered movie or show name (you'll need to implement this part)

