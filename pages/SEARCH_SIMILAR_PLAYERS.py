import streamlit as st
import time
import numpy as np
from utils import instantiate_objects,load_data
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

st.set_page_config(page_title="Compare Outfield Players", page_icon=f"{BASE_DIR}/icons/audio.png")

g_df,o_df=load_data()
def ret_similar_players(player_name,g_df,o_df):
    if player_name in o_df['Player'].values:
        knn,X_pca=instantiate_objects('outfield')
        player_index = o_df.index.get_loc(o_df[o_df['Player'] == player_name].index[0])
        # print(player_index)
        player_pca=X_pca[player_index].reshape(1,-1)
        distances, indices = knn.kneighbors(player_pca, n_neighbors=4)
        distances = list(distances[0][1:4])
        # distances.append(0)#so that the players own distance is made 0
        indices = list(indices[0][1:4])
        # print(indices)
        # indices.append(player_index)
        # print(indices)
        req_cols=['Player','Nation','Pos','Squad','Comp','Age']
        similar_players=o_df.iloc[indices][req_cols]
        similar_players['Similarity']=distances
        # print(type(similar_players))
        return similar_players
    else :
        knn,X_pca=instantiate_objects('goalkeeper')
        player_index = g_df.index.get_loc(g_df[g_df['Player'] == player_name].index[0])
        # print(player_index)
        player_pca=X_pca[player_index].reshape(1,-1)
        distances, indices = knn.kneighbors(player_pca, n_neighbors=4)
        distances = list(distances[0][1:4])
        # distances.append(0)#so that the players own distance is made 0
        indices = list(indices[0][1:4])
        # print(indices)
        # indices.append(player_index)
        # print(indices)
        req_cols=['Player','Nation','Pos','Squad','Comp','Age']
        similar_players=g_df.iloc[indices][req_cols]
        similar_players['Similarity']=distances
        print(type(similar_players))
        return similar_players

st.set_page_config(page_title="Plotting Demo2", page_icon="")

st.markdown("# Similarity Search")
st.sidebar.header("Similarity Search")
player=st.sidebar.selectbox("Select Player to search",g_df['Player'].to_list()+o_df['Player'].to_list())
similar_flag=st.sidebar.button("Generate Top 3 Similar Players")
st.markdown("""
### Discover Similar Players Using Machine Learning

Find players with comparable playing styles using advanced machine learning algorithms. 
This system employs **K-Nearest Neighbors (KNN)** to analyze multiple performance metrics 
The algorithm calculates similarity scores based on statistical patterns to identify footballers 
with matching profiles. Perfect for scouting alternatives, finding tactical replacements, or 
discovering hidden gems who mirror the characteristics of your selected player.
""")
if similar_flag:
    st.dataframe(ret_similar_players(player,g_df,o_df).style.highlight_max(subset=['Similarity']))

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")