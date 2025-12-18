import plotly.graph_objects as go
import streamlit as st
import time
import numpy as np
from utils import get_goalkeeper,get_outfield,load_data

st.set_page_config(page_title="Compare Goalkeepers", page_icon="🥅")

st.markdown("# Compare two Outfield PLayers")
st.sidebar.header("Outfield Players Comparison")
st.write(
    """
    Compare two goalkeepers on their individual statistics .
"""
)

player1=st.sidebar.selectbox("Select First GoalKeeper",get_outfield())
player2=st.sidebar.selectbox("Select Second GoalKeeper",get_outfield())

#radar chart code
compare_flag=st.checkbox("Compare Goalkeepers")
def radar(player1, player2):
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    i=0
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)
    _,df=load_data()
    categories = ['Gls','Ast','xG','xAG','Sh/90']
    i+=25
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)
    # Get integer positions
    p1_idx = df.index.get_loc(df[df['Player'] == player1].index[0])
    p2_idx = df.index.get_loc(df[df['Player'] == player2].index[0])

    # Extract stats
    player1_stats = df.iloc[p1_idx][categories].tolist()
    player2_stats = df.iloc[p2_idx][categories].tolist()

    # Create radar chart
    fig = go.Figure()
    i+=25
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)

    fig.add_trace(go.Scatterpolar(
        r=player1_stats,
        theta=categories,
        fill='toself',
        name=player1,
        line=dict(color='#ff7f0e')
    ))

    fig.add_trace(go.Scatterpolar(
        r=player2_stats,
        theta=categories,
        fill='toself',
        name=player2,
         line=dict(color='#1f77b4')
    ))
    i+=25
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(max(player1_stats), max(player2_stats)) * 1.1]  # automatic range
            )
        ),
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)
    i+=25
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)
    progress_bar.empty()

# Call the radar function
if compare_flag: 
    radar(player1, player2)

st.button("Re-run")