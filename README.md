# 🎙️ Deepfake Audio Detection Website

This project is a real-time Deepfake Audio Detection web application built with Python Flask. It uses MFCC audio features and a machine learning model to classify whether an uploaded or recorded voice is **real** or **fake**.

---

## 🚀 Features

- 🎤 Record voice directly from browser (WebRTC + JavaScript)
- 🔍 Extract 13-dimensional MFCC features
- 🧠 Predict using a trained `.pkl` model (e.g., Logistic Regression)
- 💬 Return result as **Real** or **Fake**
- 📱 (Optional) Send result to Telegram via n8n webhook
- 🌐 Can be hosted on Replit or local server

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/deepfake-audio-detector.git
cd deepfake-audio-detector


2. Install dependencies
pip install -r requirements.txt


3. Run the Flask server
python main.py
