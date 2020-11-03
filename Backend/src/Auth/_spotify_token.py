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
    """A Collection of Static Methods used to operate on SpotifyTokens.

    Following the Builder Patter, the implementation of SpotifyToken is
    separate from the Data, as the data is stored in a web session. This
    class exists solely to collect all associated methods into a namespace.

    Public Methods:
        refesh (token: SpotifyToken) -> SpotifyToken
        encrypt (token: SpotifyToken) -> bytes
        decrypt (encrypted_token: bytes) -> SpotifyToken
        get_access_token (token: SpotifyToken) -> str
    Private Methods:
        _to_bytes (token: SpotifyToken) -> bytes
    """

    @staticmethod
    def refresh(token: SpotifyToken) -> SpotifyToken:
        """Refresh the given token and return new token.

        Given a correct SpotifyToken, make a refresh request
        to accounts.spotify.com/api/token using the given Token's
        refresh code. Return the newly refeshed token.

        Parameters |     Type     | Description
        -----------|--------------|--------------------------------
        token      | SpotifyToken | A Valid SpotifyToken Dictionary

        Return a new SpotifyToken object.
        """

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
        """Return a byte array of the token.

        Given a SpotifyToken, convert it to a string
        via json.dumps, then encode that string into bytes
        via type conversion.

        Parameters |     Type     | Description
        -----------|--------------|--------------------------------
        token      | SpotifyToken | A Valid SpotifyToken Dictionary

        Return the encoded byte array.
        """

        return bytes(dumps(token), "utf-8")

    @staticmethod
    def encrypt(token: SpotifyToken) -> bytes:
        """Return an encrypted byte array of token.

        Given a SpotifyToken, convert it to bytes via
        _to_bytes, then pipe that into Fernet's encrypt
        algorithm.

        Parameters |     Type     | Description
        -----------|--------------|--------------------------------
        token      | SpotifyToken | A Valid SpotifyToken Dictionary

        Return the encrypted byte array.
        """

        encrypter = Fernet(FERNET_KEY)
        return encrypter.encrypt(TokenInterface._to_bytes(token))

    @staticmethod
    def decrypt(encypted_token: bytes) -> SpotifyToken:
        """Return a decrypted SpotifyToken given a correct byte array.

        Given a correct encrypted_token, decrypt via Fernet's decryption
        algorithm.

        Parameters      |     Type     | Description
        ----------------|--------------|--------------------------------
        encrypted_token | bytes        | An encrypted Byte Array of SpotifyToken

        Return the decrypted token.
        """

        decrypter = Fernet(FERNET_KEY)
        return loads(decrypter.decrypt(encypted_token).decode())

    @staticmethod
    def get_access_token(token: SpotifyToken) -> str:
        """Return the access_token of token.

        Given a correct SpotifyToken, return the value at key
        "access_token".

        Parameters |     Type     | Description
        -----------|--------------|--------------------------------
        token      | SpotifyToken | A Valid SpotifyToken Dictionary

        Return a string of access_token.
        """

        return str(token["access_token"])
