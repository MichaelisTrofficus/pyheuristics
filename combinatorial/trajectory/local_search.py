from typing import Callable, Union
from combinatorial.trajectory.utils.helpers import imp_best, imp_first
from combinatorial.trajectory.base import NeighborhoodStructure


class LocalSearch:
    def __init__(self,
                 objective_fn: Callable,
                 nbhd_struct: NeighborhoodStructure,
                 improve_fn: Union[str, Callable] = "first",
                 ):
        """

        Args:
            objective_fn: The objective function to be optimized
            nbhd_struct: The neighborhood stucture
            improve_fn: The improvement function (right now only 'first' and 'best' available)
        """
        self.objective_fn = objective_fn
        self.nbhd_struct = nbhd_struct
        self.improve_fn = improve_fn

    def improve(self, curr, neighbors: list):
        if self.improve_fn == "first":
            return imp_first(self.objective_fn, curr, neighbors)
        elif self.improve_fn == "best":
            return imp_best(self.objective_fn, curr, neighbors)
        else:
            return self.improve_fn(self.objective_fn, curr, neighbors)

    def search(self, init_sol, max_iter: int = 1000):
        """
        Args:
            init_sol: The initial solution
            max_iter: Maximum iterations before stopping the algorithm
        """
        curr = init_sol
        for _ in range(max_iter):
            candidate, cost = self.improve(
                curr,
                self.nbhd_struct.get_neighbors(curr)
            )
            if cost > self.objective_fn(curr):
                curr = candidate
            else:
                return curr
        return curr














