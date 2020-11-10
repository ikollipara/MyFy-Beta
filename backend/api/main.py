# api/app.py
# Ian Kollipara
# MyFy API
# Flask App

# Imports
from flask import Flask

app: Flask = Flask(__name__)

from routes import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)