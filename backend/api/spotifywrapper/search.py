# spotifywrapper/search.py
# Ian Kollipara
# 2020.11.09
# Spotify API Wrapper
# Search Endpoint

# Imports
from typing import Union, Dict, List
from requests import get
from ._globals import SearchType, AccessToken
from functools import reduce


def search(
    auth_token: AccessToken,
    query: str,
    search_type: List[SearchType],
    limit: int = 20,
    offset: int = 0,
) -> List[Dict]:
    """Return a List of objects that match the query.

    Given a correct SpotifyToken, call the Spotify API
    endpoint for search, passing in the query parameter.

    Parameters  |        Type        | Description
    ------------|--------------------|----------------------------------------------------------
    auth_token  | AccessToken        | A Valid Spotify Access Token
    query       | Str                | The text to search against
    search_type | List of SearchType | What formats to search
    limit       | Int                | Total Length of Returned List
    offset      | Int                | How many to adjust returned values by (i.e. 0-20 -> 4-24)

    Return a List Composed of Different JSON Objects.
    see https://developer.spotify.com/documentation/web-api/reference/search/search/ for more detail.
    """
    payload: Dict[str, Union[str, int]] = {
        "q": query.replace(" ", "%20"),
        "type": reduce(
            lambda a, x: a + "{},".format(x), map(lambda x: x.value, search_type), ""
        )[:-1],
        "limit": limit,
        "offset": offset,
    }

    return get(
        "https://api.spotify.com/v1/search/",
        params=payload,
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    ).json()["items"]
