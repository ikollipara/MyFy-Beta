# backend/src/Spwrapper/personalization.py
# Ian Kollipara
# 2020.10.20
# Wrapper calls for Spotify Web API
# Personalization Endpoints

# Imports
from src.Auth import TokenInterface, SpotifyToken
from ._spwrapper_globals import TimeRange
from typing import List, Dict, Union
import requests


def get_user_top_artists(
    auth_token: SpotifyToken,
    time_range: List[TimeRange],
    limit: int = 20,
    offset: int = 0,
) -> Dict[TimeRange, List]:
    """Return User Top Artists for given TimeRange(s).

    Given a correct SpotifyToken, call the Spotify
    API endpoint for Personalization, with the given
    TimeRange(s), limit, and offset. Return a Dictionary
    with TimeRanges as Keys.

    Parameters |     Type          |  Description
    -----------|-------------------|----------------------------------
    auth_token | SpotifyToken      |  A Valid Spotify Token Dictionary
    time_range | List of TimeRange |  A List of Time Ranges to query
    limit      | Int               |  Total items in each value; Default to 20
    offset     | Int               |  Adjust returned value numbers (0-20 -> 4-24)

    Return a Dictionary with Keys based upon given TimeRange(s), with values
    being lists of length limit.
    See https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/ for more detail.
    """

    top_artists: Dict[TimeRange, List] = {}

    for time in time_range:
        payload: Dict[str, Union[str, int]] = {
            "time_range": time.value,
            "limit": limit,
            "offset": offset,
        }

        top_artists.update(
            {
                time.value: requests.get(
                    "https://api.spotify.com/v1/me/top/artists",
                    params=payload,
                    headers={
                        "Authorization": f"Bearer {TokenInterface.get_access_token(auth_token)}"
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
    """Return User Top Tracks for given TimeRange(s).

    Given a correct SpotifyToken, call the Spotify
    API endpoint for Personalization, with the given
    TimeRange(s), limit, and offset. Return a Dictionary
    with TimeRanges as Keys.

    Parameters |     Type          |  Description
    -----------|-------------------|----------------------------------
    auth_token | SpotifyToken      |  A Valid Spotify Token Dictionary
    time_range | List of TimeRange |  A List of Time Ranges to query
    limit      | Int               |  Total items in each value; Default to 20
    offset     | Int               |  Adjust returned value numbers (0-20 -> 4-24)

    Return a Dictionary with Keys based upon given TimeRange(s), with values
    being lists of length limit.
    See https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/ for more detail.
    """

    top_tracks: Dict[TimeRange, List] = {}

    for time in time_range:
        payload: Dict[str, Union[str, int]] = {
            "time_range": time.value,
            "limit": limit,
            "offset": offset,
        }

        top_tracks.update(
            {
                time.value: requests.get(
                    "https://api.spotify.com/v1/me/top/tracks",
                    params=payload,
                    headers={
                        "Authorization": f"Bearer {TokenInterface.get_access_token(auth_token)}"
                    },
                ).json()["items"]
            }
        )
    return top_tracks