from espeech import app
from flask import render_template, jsonify, request, make_response
from espeak import ESpeakNG
import StringIO
import base64
import urllib
from markupsafe import Markup

@app.template_filter('urlencode')
def urlencode_filter(s):
    if type(s) == 'Markup':
        s = s.unescape()
    s = s.encode('utf8')
    s = urllib.quote_plus(s)
    return Markup(s)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == "POST":
        req = request.form
    else:
        req = request.args
    text = req.get('text','')
    
    return render_template('index.html', text = text)

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
    
    if not text:
        return jsonify(["No data"])

    text = urllib.unquote_plus(text)

    esng = ESpeakNG()
    esng.voice = 'en-us'
    wavs = esng.synth_wav(text)

    if len(wavs) == 0:
        return jsonify(["Could not general tts"])

    response = make_response(wavs)
    response.headers['Content-Type'] = 'audio/wav'
    response.headers['Content-Disposition'] = 'attachment; filename=sound.wav'

    return response