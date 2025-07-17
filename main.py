from flask import Flask, request, render_template, jsonify
import librosa
import numpy as np
import joblib
import os

app = Flask(__name__)

# 载入模型（确保是13维特征训练的模型）
model = joblib.load("deepfake_model.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio uploaded'}), 400

    audio_file = request.files['audio']
    file_path = os.path.join("audio.wav")
    audio_file.save(file_path)

    y, sr = librosa.load(file_path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc.T, axis=0).reshape(1, -1)

    pred = model.predict(mfcc_mean)[0]
    result = "real" if pred == 0 else "fake"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
