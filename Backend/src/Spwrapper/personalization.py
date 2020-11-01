# backend/src/Spwrapper/personalization.py
# Ian Kollipara
# 2020.10.20
# Wrapper calls for Spotify Web API
# Personalization Endpoints

# Imports
from src.Auth import TokenInterface
from ._spwrapper_globals import SpotifyToken, TimeRange
from typing import List, Dict, Union
import requests


def get_user_top_artists(
    auth_token: SpotifyToken,
    time_range: List[TimeRange],
    limit: int = 20,
    offset: int = 0,
) -> Dict[TimeRange, List]:
    """ Return a Dictionary, labeled by time_range, of top Artists. """

    top_artists: Dict[TimeRange, List] = {}

    for time in time_range:
        payload: Dict[str, Union[str, int]] = {
            "time_range": time.value,
            "limit": limit,
            "offset": offset,
        }

        top_artists.update(
            {
                time: requests.get(
                    "https://api.spotify.com/v1/me/top/artists",
                    params=payload,
                    headers={
                        "Authorization": TokenInterface.get_access_token(auth_token)
                    },
                ).json()["items"]
            }
        )
    return top_artists


def get_user_top_tracks(
    auth_token: SpotifyToken,
    time_range: List[TimeRange],
    limit: int = 20,
    offset: int = 0,
) -> Dict[TimeRange, List]:
    """ Return a Dictionary, labeled by time_range, of top Tracks. """

    top_tracks: Dict[TimeRange, List] = {}

    for time in time_range:
        payload: Dict[str, Union[str, int]] = {
            "time_range": time.value,
            "limit": limit,
            "offset": offset,
        }

        top_tracks.update(
            {
                time: requests.get(
                    "https://api.spotify.com/v1/me/top/tracks",
                    params=payload,
                    headers={
                        "Authorization": TokenInterface.get_access_token(auth_token)
                    },
                ).json()["items"]
            }
        )
    return top_tracks