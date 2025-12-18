import streamlit as st
import pandas as pd
import joblib
@st.cache_data
def load_data():
    goalkeeper_df=pd.read_csv('D:/StatVision/data/goalkeepers.csv')
    outfield_df=pd.read_csv('D:/StatVision/data/outfield.csv')
    return goalkeeper_df,outfield_df

@st.cache_data
def get_goalkeeper():
    goalkeeper_names=joblib.load('objects/goalkeepers.pkl')['goalkeepers']
    return goalkeeper_names

@st.cache_data
def get_outfield():
    outfield_names=joblib.load('objects/outfield.pkl')['outfield']
    return outfield_names