# app.py

import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import requests
from io import BytesIO

# Load the processed data and models
df = pd.read_csv('anime_data.csv')

with open('anime_knn_model.pkl', 'rb') as f:
    knn = pickle.load(f)

with open('anime_embeddings.pkl', 'rb') as f:
    embeddings = pickle.load(f)

# Set up the Streamlit app layout
st.set_page_config(layout="wide")
st.title("🎌 Anime Recommendation System")

# Sidebar for user input
st.sidebar.header("Search Preferences")

# Search mode selection
search_mode = st.sidebar.radio(
    "Search By:",
    ("Original Name", "English Name"),
    horizontal=True
)

# Select anime based on search mode
if search_mode == "Original Name":
    anime_list = ["Select an anime"] + df['Name'].dropna().unique().tolist()
else:
    anime_list = ["Select an anime"] + df['English name'].dropna().unique().tolist()

selected_anime = st.sidebar.selectbox("Anime Title", anime_list)

# Recommendation function
def recommend(idx):
    distances, indices = knn.kneighbors([embeddings[idx]])
    recommendations = []
    for i in indices[0][1:]:
        anime_info = df.iloc[i].to_dict()
        recommendations.append(anime_info)
    return recommendations

# Display recommendations
if st.sidebar.button("Recommend"):
    if selected_anime == "Select an anime":
        st.warning("Please select an anime to get recommendations.")
    else:
        # Get index based on selection
        if search_mode == "Original Name":
            idx = df[df['Name'] == selected_anime].index[0]
        else:
            idx = df[df['English name'] == selected_anime].index[0]

        recs = recommend(idx)

        st.subheader(f"✨ Recommendations based on **{selected_anime}**:")

        for rec in recs:
            with st.container():
                with st.container():
                    col_img, col_info = st.columns([1, 3])
                    with col_img:
                        try:
                            response = requests.get(rec['Image URL'])
                            img = Image.open(BytesIO(response.content))
                            st.image(img, use_container_width=True)
                        except:
                            st.error("Image not available")
                    with col_info:
                        # Title
                        if search_mode == "Original Name":
                            st.markdown(f"### {rec.get('Name', 'N/A')}", unsafe_allow_html=True)
                        else:
                            st.markdown(f"### {rec.get('English name', 'N/A')}", unsafe_allow_html=True)

                        # 2-column layout for details
                        col1, col2 = st.columns(2)
                        with col1:
                            if search_mode == "Original Name":
                                st.markdown(f"**English Name:** {rec.get('English name', 'N/A')}")
                            else:
                                st.markdown(f"**Original Name:** {rec.get('Name', 'N/A')}")
                            st.markdown(f"**Genres:** {rec.get('Genres', 'N/A')}")
                            st.markdown(f"**Type:** {rec.get('Type', 'N/A')}")
                            st.markdown(f"**Episodes:** {rec.get('Episodes', 'N/A')}")
                        with col2:
                            st.markdown(f"**Aired:** {rec.get('Aired', 'N/A')}")
                            st.markdown(f"**Status:** {rec.get('Status', 'N/A')}")
                            st.markdown(f"**Studios:** {rec.get('Studios', 'N/A')}")
                            st.markdown(f"**Source:** {rec.get('Source', 'N/A')}")
                            st.markdown(f"**Duration:** {rec.get('Duration', 'N/A')}")
                            st.markdown(f"**Rating:** {rec.get('Rating', 'N/A')}")

                        # Synopsis under expander
                        with st.expander("📖 Synopsis"):
                            st.write(rec.get('Synopsis', 'N/A'))

            # Draw a nice separator card
            st.markdown(
                """
                <hr style="height:2px;border:none;color:#333;background-color:#333;" />
                """,
                unsafe_allow_html=True
            )
