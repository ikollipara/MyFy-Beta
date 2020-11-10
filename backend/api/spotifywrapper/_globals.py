# spotifywrapper/_globals.py
# Ian Kollipara
# 2020.11.09
# Spotify API Wrapper
# Package Globals

# Imports
from enum import Enum


AccessToken = str


class TimeRange(Enum):
    """Time Range Enum for use in
    Personalization Endpoint Calls
    """

    SHORT = "short_term"
    MEDIUM = "medium_term"
    LONG = "long_term"


class SearchType(Enum):
    """Search Type Enum for use in
    Search Endpoint Calls
    """

    ALBUM = "album"
    ARTIST = "artist"
    PLAYLIST = "playlist"
    TRACK = "track"
    SHOW = "show"
    EPISODE = "episode"
