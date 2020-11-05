# backend/src/Spwrapper/_spwrapper_globals.py
# Ian Kollipara
# 2020.10.20
# Wrapper for Spotify Web API
# Package Globals

# Imports
from enum import Enum

# Time Range Enum for use in
# Personalization Endpoint Calls
class TimeRange(Enum):
    SHORT = "short_term"
    MEDIUM = "medium_term"
    LONG = "long_term"


# Search Type Enum for use in
# Search Endpoint Calls
class SearchType(Enum):
    ALBUM = "album"
    ARTIST = "artist"
    PLAYLIST = "playlist"
    TRACK = "track"
    SHOW = "show"
    EPISODE = "episode"


class SeedType(Enum):
    ARTIST = "seed_artists"
    GENRE = "seed_genres"
    TRACK = "seed_tracks"


SpotifyID = str