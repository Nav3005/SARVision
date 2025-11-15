# app.py
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("cap_model.keras"))

# App title
st.title("Image Captioning Part")
st.write("Upload a SAR image to get terrain, area, and vegetation description.")

# System prompt for SARVision
SYSTEM_PROMPT = """
You are SARVision, a deep learning–based system designed to interpret Synthetic Aperture Radar (SAR) satellite imagery.
Your goal is to:
1. Translate SAR images into optical-like descriptions.
2. Describe only the terrain, area, and vegetation — no man-made structures unless explicitly visible.
3. Maintain scientific clarity while keeping descriptions concise and objective.
4. Avoid speculative statements.
"""

# File uploader
uploaded_file = st.file_uploader("Upload SAR Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded SAR Image", use_column_width=True)

    # Generate caption immediately
    try:
        model = genai.GenerativeModel(model_name=os.getenv("model"))
        response = model.generate_content(
            [
                SYSTEM_PROMPT,
                image
            ]
        )
        caption = response.text.strip()
        st.subheader("Generated Caption")
        st.write(caption)
    except Exception as e:
        st.error(f"Error generating caption: {e}")