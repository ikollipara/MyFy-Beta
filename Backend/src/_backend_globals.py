# Backend/_backend_globals.py
# Ian Kollipara
# 2020.10.31
# Backend Globals

# Imports
import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(
    filemode="Backend/logs/backend.log",
    format="%(asctime)s | [%(levelname)s]: %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=40,
)
