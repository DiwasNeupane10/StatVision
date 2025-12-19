import streamlit as st

# Page configuration
st.set_page_config(page_title="StatsVision", layout="wide", page_icon="")

# Title and description
st.title("StatsVision")
st.markdown("Where passion meets precision, football analytics reimagined")

# Sidebar for chart selection and options



# Chart type selection
# chart_type = st.sidebar.selectbox(
#     "Select Chart Type",
#     ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart", "Area Chart", 
#      "Histogram", "Box Plot", "Heatmap", "3D Scatter"]
# )
# goalkeeper_names=joblib.load('objects/goalkeepers.pkl')['goalkeepers']
# outfield_names=joblib.load('objects/outfield.pkl')['outfield']
# st.sidebar.selectbox('Goalkeepers',goalkeeper_names)
# st.sidebar.selectbox('Outfield Players',outfield_names)

# Generate sample data
# @st.cache_data
# def load_data():
#     goalkeeper_df=pd.read_csv('D:/StatVision/data/goalkeepers.csv')
#     outfield_df=pd.read_csv('D:/StatVision/data/outfield.csv')
#     return goalkeeper_df,outfield_df


