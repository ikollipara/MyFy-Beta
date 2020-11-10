# api/routes.py
# Ian Kollipara
# 2020.11.09
# MyFy API
# Flask Routes

# Imports
from typing import Dict, Tuple
from flask import request
from itertools import chain
from functools import reduce
from spotifywrapper import get_user_top_artists, TimeRange
from main import app


@app.route("/listening_graph")
def get_listening_graph() -> Dict[str, Tuple[int, int]]:
    datapoints: Dict[str, Tuple[int, int]] = {}
    try:
        access_token = str(request.headers.get("access_token"))
        genre: str = str(request.args.get("genre"))

        for key, value in get_user_top_artists(
            access_token, [TimeRange.LONG, TimeRange.MEDIUM, TimeRange.SHORT], limit=50
        ).items():
            datapoints.update(
                {
                    key.value: (
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
                                chain.from_iterable(
                                    map(lambda artist: artist["genres"], value)
                                )
                            ),
                            0,
                        ),
                    )
                }
            )
        return datapoints
    except Exception as e:
        print(e)
        return datapoints


@app.route("/total_genres")
def get_total_genres() -> Dict:
    try:
        access_token = str(request.headers.get("access_token"))

        return {
            "genres": list(
                set(
                    [
                        chain.from_iterable(map(lambda artist: artist["genre"], value))
                        for value in get_user_top_artists(
                            access_token,
                            [TimeRange.LONG, TimeRange.MEDIUM, TimeRange.SHORT],
                            limit=50,
                        ).values()
                    ]
                )
            )
        }
    except Exception as e:
        print(e)
        return {"genres": []}