# backend/src/Auth/spotify_token.py
# Ian Kollipara
# 2020.10.21
# Spotify Authentication Package
# SpotifyToken Interface Implementation

# Imports
from json import dumps, loads
from ._auth_globals import SpotifyToken, FERNET_KEY, auth_logger
from cryptography.fernet import Fernet
from src import Env
import requests


class TokenInterface:
    @staticmethod
    def refresh(token: SpotifyToken) -> SpotifyToken:
        try:
            return requests.post(
                "https://accounts.spotify.com/api/token",
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": token["refresh_token"],
                    "client_id": Env.CLIENT_ID.value,
                    "client_secret": Env.CLIENT_SECRET.value,
                },
            ).json()
        except Exception as e:
            auth_logger.error("Token Refresh Failed: {}".format(e))
            return {"": ""}

    @staticmethod
    def _to_bytes(token: SpotifyToken) -> bytes:
        return bytes(dumps(token), "utf-8")

    @staticmethod
    def encrypt(token: SpotifyToken) -> bytes:
        encrypter = Fernet(FERNET_KEY)
        return encrypter.encrypt(TokenInterface._to_bytes(token))

    @staticmethod
    def decrypt(encypted_token: bytes) -> SpotifyToken:
        decrypter = Fernet(FERNET_KEY)
        return loads(decrypter.decrypt(encypted_token).decode())

    @staticmethod
    def get_access_token(token: SpotifyToken) -> str:
        return str(token["access_token"])
