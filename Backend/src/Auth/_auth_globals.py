# backend/src/Auth/auth_globals.py
# Ian Kollipara
# 2020.10.21
# Spotify Authentication Package
# Package Globals

# Imports
import logging
from typing import Dict, Union
from cryptography.fernet import Fernet

# Global Type Aliases
SpotifyToken = Dict[str, Union[str, int]]

# Global Contstants

# This Key is used in Token Encyption
FERNET_KEY = Fernet.generate_key()

# TODO: Fix Logger
auth_logger = logging.getLogger("backend.auth")