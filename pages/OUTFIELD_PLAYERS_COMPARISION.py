
import streamlit as st

import numpy as np
from utils import load_data,filter_position,detailed_stats,radar,get_idx,barchart_data

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
    
st.set_page_config(page_title="Compare Outfield Players", page_icon=f"{BASE_DIR}/icons/football-shoes.png")

st.header("Compare Outfield Players")

st.sidebar.header("Outfield Players Comparison")

position=st.sidebar.selectbox("Select a Position ",['Midfield','Defense','Forward'])
_,df=load_data()

filtered_df,filtered_names=filter_position(position,df)

st.markdown(
    """
    ##### Compare two outfield players on their individual statistics .
"""
)
player1=st.selectbox("Select First Outfield Player",filtered_names)
player2=st.selectbox("Select Second Outfield Player",filtered_names)
same_flag=True
if player1==player2:
    st.warning("Select different players")
    st.stop()
else:
    same_flag=False
comparision_cols=df.columns.tolist()
comparision_cols=[cc for cc in comparision_cols if cc not in ['Player','Nation','Pos','Squad','Comp','Age']]
select_comparision_cols=st.multiselect("Select Comparision Metrics",options=comparision_cols,max_selections=5)

display=st.checkbox("Display individual stats")
compare_flag=st.button("Compare Players")
#radar chart code




   





# Call the radar function
if compare_flag and  not(same_flag): 
    if len(select_comparision_cols) < 4:
        st.warning("Select at least 4 metrics for comparision")
    else:
        
        if display:
            col1,col2=st.columns(2)
            with col1:
                st.subheader("RADAR CHART")
                radar(player1, player2,df,select_comparision_cols)
            with col2:
                st.subheader("BAR CHART")
                data=barchart_data(player1,player2,df,select_comparision_cols)
                st.bar_chart(data)
            st.subheader("STANDARD STATS")
            player1_idx,player2_idx=get_idx(player1,df),get_idx(player2,df)
            num_cols=df.select_dtypes(include=np.number).columns
            st.dataframe(df.iloc[[player1_idx,player2_idx]].style.highlight_max(axis=0,subset=num_cols))
            stats_dict=detailed_stats('outfield')
            for key,value in stats_dict.items():
                key=key.replace('_',' ')
                st.subheader(key)
                value.insert(0,'Player')
                value_numcols=df[value].select_dtypes(include=np.number).columns
                st.dataframe(df.iloc[[player1_idx,player2_idx]][value].style.highlight_max(subset=value_numcols,axis=0))
            

st.button("Re-run")


