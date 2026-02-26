import streamlit as st
from pathlib import Path
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ------------------ LOAD ENV ------------------ #
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# ------------------ SYSTEM PROMPT ------------------ #
system_prompt = """
You are an advanced AI medical image analysis system specialized in analyzing
MRI scans, CT scans, X-rays, dermatological images, and other diagnostic images.

Provide structured report with:
1. Observations
2. Possible Conditions
3. Severity Assessment
4. Recommended Next Steps
5. Disclaimer (Not a medical diagnosis)

Maintain professional tone.
Do not provide prescriptions or drug dosages.
"""

# ------------------ GENERATION CONFIG ------------------ #
generation_config = {
    "temperature": 0.2,
    "max_output_tokens": 1024
}

# ------------------ MODEL ------------------ #
model = genai.GenerativeModel(
    "gemini-2.5-flash-lite",
    generation_config=generation_config
)

# ------------------ STREAMLIT UI ------------------ #

st.set_page_config(
    page_title="AI Medical Image Analyzer",
    layout="wide"
)

# Centered AI Doctor Image
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("AI-doctors-1.png", width=500)

st.title("🩺 AI Medical Image Analysis System")
st.info("Educational Medical AI Tool")

st.markdown("Upload a medical image (MRI, CT, X-ray, Skin Image) for AI-powered analysis.")
st.divider()

# File uploader
uploaded_file = st.file_uploader(
    "Upload Medical Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image_bytes = uploaded_file.getvalue()

    image_part = {
        "mime_type": uploaded_file.type,
        "data": image_bytes
    }

    st.image(uploaded_file, caption="Uploaded Image", width=100)

    if st.button("🔍 Analyze Image"):

        with st.spinner("Analyzing image... Please wait"):

            response = model.generate_content(
                [system_prompt, image_part]
            )

            st.subheader("📋 Medical Analysis Report")
            st.write(response.text)

st.divider()
