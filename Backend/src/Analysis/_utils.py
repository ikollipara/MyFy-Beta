# backend/src/Analysis/_utils.py
# Ian Kollipara
# 2020.11.01
# Package Utilties

# Imports
from typing import Callable
from queue import Queue


def return_to_queue(fn: Callable, q: Queue, **kwargs) -> None:
    """Put given function's return into given Queue.

    Given a function and a valid Queue, pass the rest of the
    keyword arguments into the function, putting the returned
    value into the Queue.

    Parameter |      Type       | Description
    --------------------------------------------------
    fn        | Function        | A callable function
    q         | Queue           | A Valid Queue object
    **kwargs  | Python Built-in | fn's arguments

    No return value.
    """

    q.put(fn(**kwargs))
