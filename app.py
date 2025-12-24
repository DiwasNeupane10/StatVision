import streamlit as st

# Page configuration
st.set_page_config(page_title="StatsVision", layout="wide", page_icon="⚽")

# Title and description
st.title("StatsVision")
st.markdown("Where passion meets precision, football analytics reimagined")


st.info("👉 Select a page from the sidebar to begin exploring the data.")

st.markdown("""
### 📌 About the Project

**StatsVision** is a football analytics platform focused on **data-driven player comparison**  
using **machine learning and interactive visualizations**.

This project allows you to:
- Compare **goalkeepers** using GK-specific performance metrics
- Compare **outfield players** across attacking, passing, and defensive stats
- Reduce high-dimensional football data using **PCA**
- Find **similar players** using machine learning–based distance models

---

### 🧠 Core Techniques
- **Feature Scaling & PCA** for dimensionality reduction  
- **Similarity Models** (KNN, cosine distance, Euclidean distance)
- **Position-specific feature engineering** (GK vs outfield)
- **Interactive visualizations** using Plotly & Streamlit

---

### 📊 What You Can Explore
Use the sidebar to navigate through:
- 🧤 **Goalkeeper Comparison** – performance profiles & similar GKs
- ⚽ **Outfield Player Comparison** – role-based player analysis
- 🔎 **Similar Players** – ML-powered recommendations
- 📈 **Visual Analytics** –, radar charts, and stat tables
---
""")



