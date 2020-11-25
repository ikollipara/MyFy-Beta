# api/routes.py
# Ian Kollipara
# 2020.11.09
# MyFy API
# Flask Routes

# Imports
from typing import Dict, List, Tuple, Union
from flask import request
from itertools import chain
from functools import reduce
from spotifywrapper import get_user_top_artists, TimeRange
from main import app

Error = Dict[str, Tuple]


@app.route("/listening_graph")
def get_listening_graph() -> Union[Dict[str, Union[str, Tuple[int, int]]], Error]:
    """Return Listening Graph Datapoints.

    Return a JSON containing times as keys and tuples as
    datapoint values.
    """
    datapoints: Dict[str, Union[str, Tuple[int, int]]] = {}

    try:
        access_token = str(request.args.get("access_token"))
        genre: str = str(request.args.get("genre"))

        for key, value in get_user_top_artists(
            access_token, [TimeRange.LONG, TimeRange.MEDIUM, TimeRange.SHORT], limit=50
        ).items():

            datapoints.update(
                {
                    "name": key.value,
                    "data": (
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
                    ),
                }
            )
        return datapoints
    except Exception as e:
        print(e)
        return {"Error": e.args}


@app.route("/total_genres")
def get_total_genres() -> Union[Dict[str, List[str]], Error]:
    """ Return total possible user genres. """

    try:
        access_token = str(request.args.get("access_token"))

        total_genres = []

        for time_ranges in get_user_top_artists(
            access_token, [TimeRange.LONG, TimeRange.MEDIUM, TimeRange.SHORT], limit=50
        ).values():

            for genres in map(lambda artist: artist["genre"], time_ranges):

                for genre in genres:

                    total_genres.append(genre)

        return {"genres": list(set(total_genres))}

    except Exception as e:
        return {"Error": e.args}