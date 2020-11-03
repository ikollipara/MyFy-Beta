# backend/src/Spwrapper/artist.py
# Ian Kollipara
# 2020.1101
# Spotify API Wrapper
# Artist Endpoint

# Imports
from typing import Dict, List, Union
from src.Auth import TokenInterface, SpotifyToken
import requests


def get_artist(
    auth_token: SpotifyToken, id: str
) -> Dict[str, Union[Dict[str, Union[str, None, int]], List[str], str]]:
    """Return Artist JSON for given id.

    Given a correct SpotifyToken, call the
    Spotify API endpoint for Artists, with the
    given id. Return the JSON object as a Dictionary.

    Parameters |    Type      |    Description
    -----------|--------------|----------------------------------
    auth_token | SpotifyToken | A Valid Spotify Token Dictionary
    id         | String       | A Valid Artist ID

    Return a Dictionary Object, translated from the Response JSON.
    see https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/ for more detail.
    """

    return requests.get(
        f"https://api.spotify.com/v1/artists/{id}",
        headers={
            "Authorization": f"Bearer {TokenInterface.get_access_token(auth_token)}"
        },
    ).json()
