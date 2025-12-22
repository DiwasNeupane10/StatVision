import plotly.graph_objects as go
import streamlit as st
import time
import numpy as np
from utils import load_data,get_goalkeeper,detailed_stats


    
st.set_page_config(page_title="Compare Goalkeepers", page_icon="D:/StatVision/icons/goalkeeper-glove.png")

st.markdown("# Compare two Goalkeepers")

st.sidebar.header("Goalkeeper Comparision")

df,_=load_data()

st.write(
    """
    Compare two outfield players on their individual statistics .
"""
)
player1=st.selectbox("Select First Outfield Player",get_goalkeeper())
player2=st.selectbox("Select Second Outfield Player",get_goalkeeper())
comparision_cols=df.columns.tolist()
comparision_cols=[cc for cc in comparision_cols if cc not in ['Player','Nation','Pos','Squad','Comp','Age']]
select_comparision_cols=st.multiselect("Select Comparision Metrics",options=comparision_cols,max_selections=5)
display=st.checkbox("Display individual stats")
compare_flag=st.button("Compare Players")
print(type(select_comparision_cols))
#radar chart code

def get_idx(name):
    idx=df.index.get_loc(df[df['Player'] == name].index[0])
    return idx

def radar(player1, player2,df,categories):
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    i=0
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)
    
    # categories = ['Gls','Ast','xG','xAG','Sh/90']
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

    st.plotly_chart(fig,width='stretch')
    i+=25
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)
    progress_bar.empty()





# Call the radar function
if compare_flag: 
    if len(select_comparision_cols) < 4:
        st.warning("Select at least 4 metrics for comparision")
    else:
        if display:
            st.subheader("RADAR CHART")
            radar(player1, player2,df,select_comparision_cols)
            st.subheader("STANDARD STATS")
            player1_idx,player2_idx=get_idx(player1),get_idx(player2)
            st.dataframe(df.iloc[[player1_idx,player2_idx]])
            stats_dict=detailed_stats('goalkeeper')
            for key,value in stats_dict.items():
                key=key.replace('_',' ')
                st.subheader(key)
                value.insert(0,'Player')
                value_numcols=df[value].select_dtypes(include=np.number).columns
                st.dataframe(df.iloc[[player1_idx,player2_idx]][value].style.highlight_max(subset=value_numcols,axis=0))
            

st.button("Re-run")