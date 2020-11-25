from flask import Flask, redirect, request, session
from werkzeug.wrappers import Response
from typing import Dict, Union
from json import loads
from requests import get, post
from flask_cors import CORS
from os import environ
from secrets import token_urlsafe

app = Flask(__name__)

app.config["SECRET_KEY"] = token_urlsafe(16)

CORS(app)

# ROUTES


@app.route("/")
def spotify_redirect() -> Response:
    try:
        session["redirect"] = request.args.get("redirect")
        return redirect(
            get(
                "https://accounts.spotify.com/authorize",
                params={
                    "client_id": environ["CLIENT_ID"],
                    "client_secret": environ["CLIENT_SECRET"],
                    "response_type": "code",
                    "redirect_uri": "http://localhost:8080/auth/store_token",
                    "scope": "user-top-read",
                },
            ).url
        )
    except Exception as e:
        print(e)
        return redirect("http://localhost:8080/auth/store_token")


@app.route("/store_token", methods=["GET"])
def store_token() -> Union[Response, Dict]:
    try:
        if token_code := request.args.get("code", "", type=str):
            session["token"] = post(
                "https://accounts.spotify.com/api/token",
                data={
                    "grant_type": "authorization_code",
                    "code": token_code,
                    "redirect_uri": "http://localhost:8080/auth/store_token",
                    "client_id": environ["CLIENT_ID"],
                    "client_secret": environ["CLIENT_SECRET"],
                },
            ).json()
            return redirect(session.pop("redirect"))
        else:
            raise Exception("No Token Code")

    except Exception as e:
        return {"Error": e.args}


@app.route("/get_token")
def get_token() -> Dict:
    if token := session.pop("token"):
        return token
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
                    "client_id": environ["CLIENT_ID"],
                    "client_secret": environ["CLIENT_SECRET"],
                },
            ).json()
        return {}
    except Exception as e:
        print(e)
        return {}


if __name__ == "__main__":
    app.run(host="0.0.0.0")