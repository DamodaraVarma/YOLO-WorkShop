import streamlit as st
import cv2
import numpy as np
from PIL import Image
import google.generativeai as genai

# Initialize Gemini AI
genai.configure(api_key="AIzaSyCCVFAlPBZ4nmXOEZ5XTrF9hprQ9c69b5g")

def analyze_image(image):
    """Process image and get suggestions from Gemini AI."""
    # Convert image to bytes
    img_bytes = np.array(image.convert('RGB')).tobytes()
    
    # Query Gemini AI
    response = genai.generate_text("Analyze this skin condition and provide possible insights.")
    return response

st.title("Skin Disease Detection")

# Camera input
image_file = st.camera_input("Take a picture")

# Upload image input
uploaded_file = st.file_uploader("Or upload an image", type=["jpg", "png", "jpeg"])

if image_file or uploaded_file:
    if image_file:
        image = Image.open(image_file)
    else:
        image = Image.open(uploaded_file)
    
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Get AI analysis
    with st.spinner("Analyzing..."):
        result = analyze_image(image)
    
    st.subheader("Analysis Result:")
    st.write(result)
