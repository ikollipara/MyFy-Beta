# backend/src/Analysis/_listening_graph.py
# Ian Kollipara
# 2020.11.01
# Listening Graph API Endpoint

# Imports
from typing import Dict, Tuple
from itertools import chain
from functools import reduce
from src.Spwrapper import get_user_top_artists, TimeRange
from src.Auth import TokenInterface
from src import app
import flask


@app.route("/api/listening_graph")
def get_listening_graph():

    flask.session["token"] = TokenInterface.encrypt(
        TokenInterface.refresh(TokenInterface.decrypt(flask.session["token"]))
    )

    try:
        listening_graph_datapoints: Dict[str, Tuple[int, int]] = {}
        user_access_token = TokenInterface.decrypt(flask.session["token"])
        genre: str = flask.request.args.get("genre")

        for key, value in get_user_top_artists(
            user_access_token, [TimeRange.LONG, TimeRange.MEDIUM, TimeRange.SHORT]
        ).items():

            listening_graph_datapoints[key] = (
                # This counts all the appearences of the given genre
                # for each artist
                reduce(
                    lambda acc, _: acc + 1,
                    filter(
                        lambda artist: genre in artist["genres"]
                        or genre in "".join(chain(artist["genres"])),
                        value,
                    ),
                    0,
                ),
                # This function counts the total unique genres present in
                # all artists
                reduce(
                    lambda acc, _: acc + 1,
                    set(
                        chain.from_iterable(map(lambda artist: artist["genres"], value))
                    ),
                    0,
                ),
            )

        return listening_graph_datapoints

    except Exception as e:
        print(e)
        return {}
