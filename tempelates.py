import streamlit as st
import requests
import time
from PIL import Image
from io import BytesIO


def generate_image(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    HEADERS = {"Authorization": "Bearer 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"}  # Replace with your API key

    with st.spinner("Generating Image..."):
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})

        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))  # Convert response to image
            st.image(image, caption=prompt)
        else:
            st.error(f"❌ Image generation failed! Error Code: {response.status_code}")
            st.write(response.text)  # Print error details

st.title("✨ Choose a Prompt to Generate an Image ✨")

animals, vehicles, robots, scenery, house = st.columns(5)

with animals:
    if st.button("Elephants running from a jungle"):
        generate_image("Some elephants running from the jungle, a lion chasing them")

with vehicles:
    if st.button("Highly modified Bugatti"):
        generate_image("Generate an image of a highly modified Bugatti")

with robots:
    if st.button("Futuristic Robots in Restaurants"):
        generate_image("Futuristic robots working in a high-tech restaurant")

with scenery:
    if st.button("Beautiful Scenery"):
        generate_image("A breathtaking scenic view of mountains and a river")

with house:
    if st.button("800 Yards Mansion"):
        generate_image("A luxurious 800 yards mansion with a pool and garden")

fantasy, city, Ancivilization, frobot, magcreature = st.columns(5)

with fantasy:
    if st.button("Mystical Floating Island"):
        generate_image("A mystical floating island with waterfalls, glowing trees, and a giant moon")

with city:
    if st.button("Futuristic Neon City"):
        generate_image("A futuristic neon-lit city with flying cars and holographic billboards at night")

with Ancivilization:
    if st.button("Lost Jungle City"):
        generate_image("A lost city in the jungle, covered in vines, with golden temples and mysterious artifacts")

with frobot:
    if st.button("Advanced Humanoid Robot"):
        generate_image("A highly advanced humanoid robot with sleek metallic armor and glowing blue eyes")

with magcreature:
    if st.button("Majestic Dragon"):
        generate_image("A majestic dragon with shimmering scales breathing blue fire in the sky")

