from flask import Flask, redirect, request
from werkzeug.wrappers import Response
from typing import Dict
from json import loads
from requests import get, post

app = Flask(__name__)

# ROUTES


@app.route("/")
def spotify_redirect() -> Response:
    try:
        return redirect(
            get(
                "https://accounts.spotify.com/authorize",
                params={
                    "client_id": "",
                    "client_secret": "",
                    "response_type": "code",
                    "redirect_uri": "http://localhost:8000/auth/spotifytoken",
                    "scope": "user-top-read",
                },
            ).url
        )
    except Exception as e:
        print(e)
        return redirect("http://localhost:8000/auth/spotifytoken")


@app.route("/spotifytoken", methods=["GET"])
def get_token() -> Dict:
    try:
        if token_code := request.args.get("code"):
            return post(
                "https://accounts.spotify.com/api/token",
                data={
                    "grant_type": "authorization_code",
                    "code": token_code,
                    "redirect_uri": "http://localhost:8000/auth/spotifytoken",
                    "client_id": "",
                    "client_secret": "",
                },
            ).json()
        return {}
    except Exception as e:
        print(e)
        return {}


@app.route("/refresh", methods=["GET"])
def refresh_token() -> Dict:
    try:
        if token := request.headers.get("token"):
            return post(
                "https://accounts.spotify.com/api/token",
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": loads(token)["refresh_token"],
                    "client_id": "",
                    "client_secret": "",
                },
            ).json()
        return {}
    except Exception as e:
        print(e)
        return {}


if __name__ == "__main__":
    app.run(host="0.0.0.0")