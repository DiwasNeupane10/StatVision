import streamlit as st

# Page configuration
st.set_page_config(page_title="StatsVision", layout="wide", page_icon="")

# Title and description
st.title("StatsVision")
st.markdown("Where passion meets precision, football analytics reimagined")


st.info("👉 Select a page from the sidebar to begin exploring the data.")

st.markdown("""
### 📌 About the Project

**StatsVision** is a football analytics platform focused on **player performance analysis**  
using **data-driven and machine learning techniques**.

This project aims to:
- Analyze player statistics across multiple dimensions
- Reduce high-dimensional football data using **PCA**
- Identify **similar players** using clustering & distance-based models
- Provide **interactive visualizations** for analysts and fans

---

### 🧠 Key Techniques Used
- **Feature Scaling & PCA** for dimensionality reduction  
- **Clustering / Similarity Models** (KNN, cosine distance, etc.)
- **Interactive Visualizations** using Plotly & Streamlit
- Position-specific analysis (e.g., **Goalkeepers vs Outfield players**)

---

### 📊 What You Can Explore
Use the sidebar to navigate through:
- 🔍 **Player Analysis** – compare and visualize players
- 🧤 **Goalkeeper Analysis** – GK-specific metrics & similarity
---
""")



