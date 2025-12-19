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


'''
model_obj={
    'standard_scaler':standard_scaler,
    'pca':pca,
    'knn':outfield_nn
}
'''
@st.cache_data
def instantiate_objects(type):
    match type:
        case 'outfield':
            model_object=joblib.load('D:/StatVision/objects/outfield_nn_model.pkl')
            X_pca=joblib.load('D:/StatVision/objects/outfield_pca.pkl')['outfield_pca']
            knn=model_object['knn']
            return knn,X_pca
        case 'goalkeeper':
            model_object=joblib.load('D:/StatVision/objects/goalkeeper_nn_model.pkl')
            X_pca=joblib.load('D:/StatVision/objects/goalkeeper_pca.pkl')['goalkeeper_pca']
            knn=model_object['knn']
            return knn,X_pca


def filter_position(position,df):
    position_map={
        'Midfield':'MF',
        'Defense':'DF',
        'Forward':'FW'
    }
    position=position_map[position]
    filtered_df = df[df['Pos'].str.contains(position, na=False)]
    filtered_names=filtered_df['Player'].tolist()
    return filtered_df,filtered_names

