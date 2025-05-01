import assemblyai as aai
from dotenv import load_dotenv
import openai
import os
from flask import Flask, render_template, jsonify, request

load_dotenv()
API_KEY = os.getenv("Assembly_AI_KEY")

aai.settings.api_key = API_KEY

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static"

@app.route('/', methods = ['GET', 'POST'])
def main():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            audio_file = open("static/Assm.mp3", "rb")
            config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)
            transcript = aai.Transcriber(config=config).transcribe(audio_file)

            response = [{"role": "user", "content": transcript.text}]

        return jsonify(response)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)