# Backend/src/Spwrapper/browse.py
# Ian Kollipara
# 2020.11.05
# Spotify API Wrapper
# Browse Enpoint

# Imports
import flask
import requests
from typing import List, Dict, Union
from functools import reduce
from Backend.src.Auth import SpotifyToken, TokenInterface
from ._spwrapper_globals import SpotifyID, SeedType


def get_reccomendations(
    auth_token: SpotifyToken, seeds: Dict[SeedType, SpotifyID], limit: int = 10
) -> Dict:

    payload: Dict[str, Union[str, int]] = {"limit": limit}

    for key, value in seeds.items():
        payload.update(
            (key.value, reduce(lambda acc, item: acc + f"{item},", value, ""))[:-1]
        )

    return requests.get(
        "https://api.spotify.com/v1/reccomendations",
        params=payload,
        headers={
            "Authorization": f"Bearer {TokenInterface.get_access_token(auth_token)}"
        },
    ).json()
