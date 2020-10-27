# Auth/spotify_token.py
# Ian Kollipara
# 2020.10.21
# MyFy Spotify Authentication
# SpotifyToken Interface Implementation

from json import dumps, loads
from .auth_globals import SpotifyToken, FERNET_KEY
from cryptography.fernet import Fernet
import requests


class Interface:
    @staticmethod
    def refresh(token: SpotifyToken) -> SpotifyToken:
        new_token: SpotifyToken = requests.post(
            "https://accounts.spotify.com/api/token",
            data={"grant_type": "refresh_token", "refresh_token": token._refresh_token},
            header={"Authorization": AUTH_GLOBALS.BASIC_KEY},
        ).json()

        return new_token

    @staticmethod
    def _to_bytes(token: SpotifyToken) -> bytes:
        return bytes(dumps(token), "utf-8")

    @staticmethod
    def encrypt(token: SpotifyToken) -> bytes:
        encrypter = Fernet(FERNET_KEY)
        return encrypter.encrypt(Interface._to_bytes(token))

    @staticmethod
    def decrypt(encypted_token: bytes) -> SpotifyToken:
        decrypter = Fernet(FERNET_KEY)
        return loads(decrypter.decrypt(encypted_token).decode())

    @staticmethod
    def get_access_token(token: SpotifyToken) -> str:
        return token["access_token"]
