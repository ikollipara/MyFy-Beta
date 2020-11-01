# Auth/routes.py
# Ian Kollipara
# 2020.10.27
# Spotify Auth Package
# Flask Endpoints/Routes

# Imports
import flask
import requests
from ._spotify_token import TokenInterface
from werkzeug.wrappers import Response
from ._auth_globals import auth_logger
from src import app, Env


@app.route("/auth")
def get_spotify_redirect() -> Response:
    try:
        print(Env.CLIENT_ID.value)
        print(Env.CLIENT_SECRET.value)
        return flask.redirect(
            requests.get(
                "https://accounts.spotify.com/authorize",
                params={
                    "client_id": Env.CLIENT_ID.value,
                    "client_secret": Env.CLIENT_SECRET.value,
                    "response_type": "code",
                    "redirect_uri": "http://localhost:5050/auth/spotifytoken",
                    "scope": "user-top-read",
                },
            ).url
        )
    except Exception as e:
        auth_logger.error("Failed to Send in Token Request: {}".format(e))
        return flask.redirect("/")


@app.route("/auth/spotifytoken")
def get_raw_token() -> Response:
    try:
        token_code = flask.request.args.get("code")

        if token_code:

            flask.session["token"] = TokenInterface.encrypt(
                requests.post(
                    "https://accounts.spotify.com/api/token",
                    data={
                        "grant_type": "authorization_code",
                        "code": token_code,
                        "redirect_uri": "http://localhost:5050/auth/spotifytoken",
                        "client_id": Env.CLIENT_ID.value,
                        "client_secret": Env.CLIENT_SECRET.value,
                    },
                ).json()
            )
    except Exception as e:
        auth_logger.error("No Spotify Redirect Code: {}".format(e))

    return flask.redirect("/")