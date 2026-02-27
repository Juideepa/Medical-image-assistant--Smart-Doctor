🩺 AI Medical Image Analysis System

An AI-powered Medical Image Analysis Web Application built using Google Gemini 2.5 Flash-Lite (Vision Model) and Streamlit.

The system allows users to upload medical images such as MRI scans, CT scans, X-rays, and dermatological images, and generates a structured AI-based medical report using advanced prompt engineering.

🔗 Live Demo:
👉 https://medical-image-assistant--smart-doctor-juideepa.streamlit.app/

⚠️ This project is for educational purposes only and does not replace professional medical advice.

🚀 Features

🖼️ Upload medical images (JPG, JPEG, PNG)

🧠 Multimodal AI analysis using Gemini Vision

📋 Structured Medical Report:

Observations

Possible Conditions

Severity Assessment

Recommended Next Steps

Medical Disclaimer

🔐 Secure API key handling via .env

🌐 Deployed on Streamlit Cloud

🎨 Clean and responsive UI

🛠️ Tech Stack

Python

Streamlit

Google Gemini API (2.5 Flash-Lite)

python-dotenv

Pillow

🧠 How It Works

User uploads a medical image.

The image is processed and sent to Gemini Vision model.

A structured medical prompt guides the AI analysis.

The model generates a professional-style medical report.

Results are displayed in a clean Streamlit interface.

🌍 Deployment

This application is deployed using Streamlit Community Cloud.

To deploy:

Push code to GitHub

Add requirements.txt

Add secrets in Streamlit Cloud (GEMINI_API_KEY)

Deploy directly from repository
