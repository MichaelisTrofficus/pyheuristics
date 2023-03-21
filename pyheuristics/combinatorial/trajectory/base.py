import abc
from abc import ABC


class TrajectoryMethod(ABC):
    """
    Abstract Base Class for Trajectory Methods.
    """

    @abc.abstractmethod
    def objective_fn(self, sol):
        raise NotImplementedError

    @abc.abstractmethod
    def get_neighbors(self, sol):
        raise NotImplementedError

    @abc.abstractmethod
    def run(self, **kwargs):
        raise NotImplementedError
