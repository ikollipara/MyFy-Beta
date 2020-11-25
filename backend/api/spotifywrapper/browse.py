# Backend/src/Spwrapper/browse.py
# Ian Kollipara
# 2020.11.05
# Spotify API Wrapper
# Browse Enpoint

# Imports
from requests import get
from typing import Dict, Union
from functools import reduce
from ._globals import AccessToken, SpotifyID, SeedType

def get_reccomendations(
    auth_token: AccessToken, seeds: Dict[SeedType, SpotifyID], limit: int = 10
) -> Dict:

    payload: Dict[str, Union[str, int]] = {"limit": limit}

    for key, value in seeds.items():
        payload.update(
            (key.value, reduce(lambda acc, item: acc + f"{item},", value, ""))[:-1]
        )

    return get(
        "https://api.spotify.com/v1/reccomendations",
        params=payload,
        headers={
            "Authorization": f"Bearer {auth_token}"
        },
    ).json()
