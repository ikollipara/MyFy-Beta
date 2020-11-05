# backend/src/_backend_globals.py
# Ian Kollipara
# 2020.10.31
# Backend Globals

# Imports
import logging
from flask import Flask

# Flask App Instance
app = Flask(__name__)

Display = {"Test": "http://localhost:5050"}

# TODO Fix Logging
logging.basicConfig(
    filemode="Backend/logs/backend.log",
    format="%(asctime)s | [%(levelname)s]: %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=40,
)