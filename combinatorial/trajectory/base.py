import abc
from abc import ABCMeta


class NeighborhoodStructure(ABCMeta):
    """
    Abstract Base Class for defining Neighborhood Structures. Simply implement
    method `get_neighbors`, which will receive the current solution and will
    return a list of neighbors
    """

    @abc.abstractmethod
    def get_neighbors(self, sol) -> list:
        raise NotImplementedError
