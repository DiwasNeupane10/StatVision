import streamlit as st
import pandas as pd
import joblib
import time
import plotly.graph_objects as go
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

@st.cache_data
def instantiate_clusters():
    goalkeeper_cluster=joblib.load('D:/StatVision/objects/goalkeepercluster_obj.pkl')
    outfield_cluster=joblib.load('D:/StatVision/objects/outfieldcluster_obj.pkl')
    return goalkeeper_cluster,outfield_cluster


@st.cache_data
def detailed_stats(case):
    if case=='outfield':
        outfield_stats={
        'SHOOTING':['Gls', 'Ast', 'G-PK', 'PK', 'PKatt', 'xG', 'npxG', 'xAG', 'G-xG', 'np:G-xG', 'Sh', 'SoT', 'Sh/90','SoT/90', 'FK'],
        'PASSING':[ 'Cmp', 'Att', 'Cmp%', 'TotDist', 'PrgDist', 'xA', 'A-xAG', 'KP', '1/3', 'PPA',
                    'CrsPA'],
        'PASS_TYPE':['Live', 'TB', 'Sw', 'Crs', 'In', 'Out', 'Str', 'PrgC', 'PrgP', 'PrgR', 'SCA90', 'PassLive',
                        'PassDead'],
        'DEFENSIVE_ACTIONS':['TO', 'Sh_stats_gca', 'Fld', 'Def', 'GCA90', 'Tkl', 'TklW', 'Def 3rd', 'Mid 3rd',
                        'Att 3rd', 'Lost','Blocks_stats_defense','Int', 'Clr', 'Err',],
        'POSSESION':[ 'Touches', 'Def Pen',
                            'Att Pen', 'Succ', 'Tkld', 'Carries', 'CPA', 'Mis', 'Dis', 'Rec']
        }
        return outfield_stats
    else:
        goalkeeper_stats={
        'SWEEPER':['AvgDist','#OPA'],
        'PERFORMANCE':['GA','GA90','SoTA','Saves','CS','PSxG'],
        'PENALTY':['PKA','PKsv','PKm'],
        'PASSES':['Att (GK)','Thr','Launch%','AvgLen'],
        'GOALKICKS':['Opp','Stp','Stp%'],

        }
        return goalkeeper_stats
    

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
    p1_idx = get_idx(player1,df)
    p2_idx =get_idx(player2,df)

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


def get_idx(name,df):
    idx=df.index.get_loc(df[df['Player'] == name].index[0])
    return idx
