from espeech import app
from flask import render_template, jsonify, request
from espeak import ESpeakNG

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voices', methods = ['GET'])
def get_voices():
    esng = ESpeakNG()
    voices = []
    for v in esng.voices:
        voices.append({"gender":v["gender"], "language":v["language"], "name":v["voice_name"].replace('_',' ')})
    return jsonify(voices)

@app.route('/tts', methods = ['GET','POST'])
def get_tts():
    if request.method == "POST":
        req = request.form
    else:
        req = request.args
    text = req.get('text','')
    
    return jsonify({"text":str(text)})