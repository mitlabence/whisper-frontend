from flask import Flask, render_template, request
import ffmpeg
import os
import requests
from werkzeug.utils import secure_filename

def convert_webm_to_mp3(input_path, output_path):
    ffmpeg.input(input_path).output(output_path, format='mp3', acodec='libmp3lame').run(overwrite_output=True)

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['audio_data']
    filename = secure_filename(file.filename)
    wav_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(wav_path)

    # Convert to MP3
    mp3_path = wav_path.replace(".webm", ".mp3")
    convert_webm_to_mp3(wav_path, mp3_path)
    os.remove(wav_path)

    # Send to transcription server
    with open(mp3_path, 'rb') as f:
        files = {'audio': (os.path.basename(mp3_path), f, 'audio/mpeg')}
        response = requests.post("http://localhost:5000/transcribe", files=files)
    
    return {"status": "ok", "transcription_response": response.text}

if __name__ == '__main__':
    app.run(debug=True)
