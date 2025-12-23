import plotly.graph_objects as go
import streamlit as st
import time
import numpy as np
from utils import load_data,get_goalkeeper,detailed_stats,radar,get_idx


    
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

#radar chart code









# Call the radar function
if compare_flag: 
    if len(select_comparision_cols) < 4:
        st.warning("Select at least 4 metrics for comparision")
    else:
        if display:
            st.subheader("RADAR CHART")
            radar(player1, player2,df,select_comparision_cols)
            st.subheader("STANDARD STATS")
            player1_idx,player2_idx=get_idx(player1,df),get_idx(player2,df)
            st.dataframe(df.iloc[[player1_idx,player2_idx]])
            stats_dict=detailed_stats('goalkeeper')
            for key,value in stats_dict.items():
                key=key.replace('_',' ')
                st.subheader(key)
                value.insert(0,'Player')
                value_numcols=df[value].select_dtypes(include=np.number).columns
                st.dataframe(df.iloc[[player1_idx,player2_idx]][value].style.highlight_max(subset=value_numcols,axis=0))
            

st.button("Re-run")