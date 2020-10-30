# Spwrapper/search.py
# Ian Kollipara
# 2020.10.29
# Wrapper calls for Spotify Web API
# Search Endpoint

# Imports
from typing import Dict, List, Union
from ._spwrapper_globals import SpotifyToken, SearchType
from Backend.Auth import TokenInterface
import requests
import functools


def search(
    auth_token: SpotifyToken,
    query: str,
    search_type: List[SearchType],
    limit: int = 20,
    offset: int = 0,
) -> Dict:

    payload: Dict[str, Union[str, int]] = {
        "q": query.replace(" ", "%20"),
        "type": functools.reduce(
            lambda a, x: a + "{},".format(x), map(lambda x: x.value, search_type), ""
        )[:-1],
        "limit": limit,
        "offset": offset,
    }

    return requests.get(
        "https://api.spotify.com/v1/search/",
        params=payload,
        headers={
            "Authorization": "Bearer {}".format(
                TokenInterface.get_access_token(auth_token)
            )
        },
    ).json()
