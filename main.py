import streamlit as st

# Set page config (optional)
st.set_page_config(page_title="DeepVision", page_icon="🔍", layout="wide")

# Main content
st.title("Welcome to DeepVision")
st.write("AI-powered image generation at its best! 🚀")

c1,c2,c3 = st.columns(3)
with c1:
    st.image("static/image1.webp")
with c2:
    st.image("static/image2.webp")
with c3:
    st.image("static/image3.webp")
c4,c6 = st.columns(2)
with c4:
    st.image("static/image4.webp")
with c6:
    st.image("static/image6.webp")
c7,c8,c9 = st.columns(3)
with c7:
    st.image("static/image7.webp")
with c8:
    st.image("static/image8.webp")
with c9:
    st.image("static/image9.webp")
