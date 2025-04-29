import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load and cache the dataset from file
    """
    df = pd.read_csv(r"D:\Kuliah\Semester 6\NLP\uts\data\train_preprocess.csv", sep=';')
    return df
