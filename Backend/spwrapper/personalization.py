# spwrapper/personalization.py
# Ian Kollipara
# 2020.10.20
# Wrapper calls for Spotify Web API
# Personalization Section

# Imports
from .spwrapper_globals import SpotifyToken
from typing import Any, List, Dict, Union
import requests


def parse_spotify_json(spotify_json: Dict) -> List:
    """ Parse the given JSON and return inner results. """
    return spotify_json["items"]


def get_user_top_artists(
    auth_token: SpotifyToken, time_range: List[str], limit: int = 20, offset: int = 0
) -> Dict[str, List]:
    """ Return a Dictionary, labeled by time_range, of top Artists. """

    top_artists: Dict[str, List] = {}

    for time in time_range:
        payload: Dict[str, Union[str, int]] = {
            "time_range": time,
            "limit": limit,
            "offset": offset,
        }

        top_artists.update(
            {
                time: parse_spotify_json(
                    requests.get(
                        "https://api.spotify.com/v1/me/top/artists",
                        params=payload,
                        headers={"Authorization": auth_token.access},
                    ).json()
                )
            }
        )
    return top_artists


def get_user_top_tracks(
    auth_token: SpotifyToken, time_range: List[str], limit: int = 20, offset: int = 0
) -> Dict[str, List]:
    """ Return a Dictionary, labeled by time_range, of top Tracks. """

    top_tracks: Dict[str, List] = {}

    for time in time_range:
        payload: Dict[str, Union[str, int]] = {
            "time_range": time,
            "limit": limit,
            "offset": offset,
        }

        top_tracks.update(
            {
                time: parse_spotify_json(
                    requests.get(
                        "https://api.spotify.com/v1/me/top/tracks",
                        params=payload,
                        headers={"Authorization": auth_token.access},
                    ).json()
                )
            }
        )
    return top_tracks