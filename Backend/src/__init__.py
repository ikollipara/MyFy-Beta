# backend/src/__init__.py
# Ian Kollipara
# 2020.10.31
# Flask Source Code Package

# Package Exports
from ._backend_globals import *
from ._env import Env, Config

# Configuring Flask Instance
app.config.from_object(Config)

# Loading Flask Routes
from .Auth._routes import *