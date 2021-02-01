import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))
from espeech import app

if __name__ == '__main__':
    app.run(debug=True)
