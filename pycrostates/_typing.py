"""Typing with ABC class for pycrostates classes.

The type class can be used for type hinting for pycrostates classes that are at
risk of circular imports, or for short-cut types re-grouping different types.
"""

from abc import ABC
from typing import Optional, Union

from numpy.random import Generator, RandomState
from numpy.typing import NDArray

from .segmentation._base import _BaseSegmentation

class CHData(ABC):
    """Typing for CHData."""

    pass


class CHInfo(ABC):
    """Typing for CHInfo."""

    pass


class Cluster(ABC):
    """Typing for a clustering class."""

    pass


class Segmentation(_BaseSegmentation):
    """Typing for a clustering class."""

    pass


RANDomState = Optional[Union[int, RandomState, Generator]]
Picks = Optional[Union[str, NDArray[int]]]
