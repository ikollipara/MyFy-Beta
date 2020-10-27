# Auth/auth_globals.py
# Ian Kollipara
# 2020.10.21
# Spotify Authentication Package
# Package Globals

from typing import Dict, Union
from cryptography.fernet import Fernet

# Global Types

SpotifyToken = Dict[str, Union[str, int]]

# Global Contstants

FERNET_KEY = Fernet.generate_key()