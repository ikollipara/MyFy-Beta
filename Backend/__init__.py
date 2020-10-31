# Backend/__init__.py
# Ian Kollipara
# 2020.10.31
# Backend Flask App Init

from flask import Flask

app = Flask(__name__)

from Backend.Auth import _routes