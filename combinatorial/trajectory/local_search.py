import abc
from abc import ABCMeta
from combinatorial.trajectory.utils.helpers import imp_best, imp_first


class LocalSearch(metaclass=ABCMeta):
    """
    Implementation of LocalSearch algorithm
    """

    def __init__(self, init_sol, improve_strategy="first"):
        self.init_sol = init_sol
        self.improve_strategy = improve_strategy

    def improve(self, curr, neighbors: list):
        if self.improve_strategy == "first":
            return imp_first(self.objective_fn, curr, neighbors)
        elif self.improve_strategy == "best":
            return imp_best(self.objective_fn, curr, neighbors)
        else:
            raise NotImplementedError("improve_mehod must be one of ['first', 'best']")

    @abc.abstractmethod
    def objective_fn(self, sol):
        raise NotImplementedError

    @abc.abstractmethod
    def get_neighbors(self, sol):
        raise NotImplementedError

    def search(self, max_iter: int = 1000):
        """
        Args:
            init_sol: The initial solution
            max_iter: Maximum iterations before stopping the algorithm
        """
        curr = self.init_sol
        for _ in range(max_iter):
            candidate, cost = self.improve(curr, self.get_neighbors(curr))
            if cost > self.objective_fn(curr):
                curr = candidate
            else:
                return curr
        return curr
