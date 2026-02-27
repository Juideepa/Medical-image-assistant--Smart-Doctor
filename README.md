🩺 AI Medical Image Analysis System

An AI-powered Medical Image Analysis application built using Google Gemini (Multimodal Vision Model) and Streamlit.

This system allows users to upload medical images (MRI, CT scan, X-ray, dermatological images, etc.) and generates a structured medical-style analysis report using prompt-engineered generative AI.

🚀 Features

📤 Upload medical images (JPG, PNG, JPEG)

🧠 AI-based multimodal image understanding using Gemini

📋 Structured medical-style report generation

⚡ Fast inference with Gemini 2.5 Flash-Lite

🔐 Secure API key management using .env

🎨 Clean and professional Streamlit UI

🛠️ Tech Stack

Frontend/UI: Streamlit

AI Model: Google Gemini 2.5 Flash-Lite

Backend Logic: Python

Environment Management: python-dotenv

Version Control: Git & GitHub

📂 Project Structure
medical-ai/
│
├── app.py
├── ai_doctor.png
├── requirements.txt
├── .gitignore
├── README.md
├── .env   (not uploaded to GitHub)
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add API Key

Create a .env file in the root folder:

GEMINI_API_KEY=your_api_key_here

⚠️ Do not upload .env to GitHub.

5️⃣ Run the Application
streamlit run app.py

The app will open in your browser.

🧠 How It Works

User uploads a medical image.

The image is sent to Gemini's multimodal model.

A structured medical analysis prompt is applied.

The AI generates:

Observations

Possible Conditions

Severity Assessment

Recommended Next Steps

Disclaimer

The output is displayed in a clean medical-report format.
