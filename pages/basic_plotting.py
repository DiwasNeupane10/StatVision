import streamlit as st
import time
import numpy as np
from utils import instantiate_outfield_objects,load_data

def ret_similar_players(player_name):
    _,df=load_data()
    if player_name in df['Player'].values:
        knn,X_pca=instantiate_outfield_objects()
        player_index = df.index.get_loc(df[df['Player'] == player_name].index[0])
        print(player_index)
        player_pca=X_pca[player_index].reshape(1,-1)
        distances, indices = knn.kneighbors(player_pca, n_neighbors=4)
        distances = list(distances[0][1:4])
        distances.append(0)#so that the players own distance is made 0
        indices = list(indices[0][1:4])
        print(indices)
        indices.append(player_index)
        print(indices)
        req_cols=['Player','Nation','Pos','Squad','Comp','Age']
        similar_players=df.iloc[indices][req_cols]
        similar_players['Similarity']=distances
        print(type(similar_players))
        return similar_players

st.set_page_config(page_title="Plotting Demo2", page_icon="")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

st.dataframe(ret_similar_players('Marc Casado').style.highlight_max(subset=['Similarity']))

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")