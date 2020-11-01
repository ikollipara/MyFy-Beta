# Spwrapper/spwrapper_types.py
# Ian Kollipara
# 2020.10.20
# Wrapper for Spotify Web API
# Package Globals

# Imports
from enum import Enum
from Backend.src.Auth import auth_globals

SpotifyToken = auth_globals.SpotifyToken


class TimeRange(Enum):
    SHORT = "short_term"
    MEDIUM = "medium_term"
    LONG = "long_term"


class SearchType(Enum):
    ALBUM = "album"
    ARTIST = "artist"
    PLAYLIST = "playlist"
    TRACK = "track"
    SHOW = "show"
    EPISODE = "episode"
