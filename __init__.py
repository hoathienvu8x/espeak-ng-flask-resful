from flask import Flask
from flask_htmlmin import HTMLMIN

app = Flask(__name__)
app.config['MINIFY_HTML'] = True
htmlmin = HTMLMIN(app)

from espeech import views
