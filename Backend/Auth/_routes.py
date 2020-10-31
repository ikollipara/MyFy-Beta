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
from Backend import app


@app.route("/auth")
def get_spotify_redirect() -> Response:
    try:
        return flask.redirect(
            requests.get(
                "https://accounts.spotify.com/authorize",
                params={
                    "client_id": "",
                    "client_secret": "",
                    "response_type": "code",
                    "redirect_uri": flask.url_for("auth/spotifytoken"),
                    "scope": "",
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
                        "redirect_uri": "",
                        "client_id": "",
                        "client_secret": "",
                    },
                ).json()
            )
    except Exception as e:
        auth_logger.error("No Spotify Redirect Code: {}".format(e))

    return flask.redirect("/")