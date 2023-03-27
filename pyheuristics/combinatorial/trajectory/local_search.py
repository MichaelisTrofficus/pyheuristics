from abc import ABC
from typing import Any

from pyheuristics.combinatorial.trajectory.base import TrajectoryMethod
from pyheuristics.execution_result import ExecutionResult


class LocalSearch(TrajectoryMethod, ABC):
    def __init__(self, init_sol: Any):
        """
        Implementation of the LocalSearch algorithm

        Args:
            init_sol: The initial solution, i.e., the starting point of the trajectory. This parameter
                can be anything: a string, an array, a graph, etc. Basically, the data structure that best
                represents a solution to the problem.
        """
        self.sol, self.cost = self._get_sol_and_cost(init_sol)

    def run(self, max_iter: int = 1000, verbose=0, history=False) -> ExecutionResult:
        """
        Args:
            max_iter: Maximum iterations before stopping the algorithm
            verbose: If verbose > 0 then print running information
            history: If `True` then return an array containing a history of costs.
        """
        history_arr = []

        if history:
            history_arr.append(self.cost)

        for i in range(max_iter):
            candidate_sol, candidate_cost = self._get_sol_and_cost(self.move())

            if self.cost - candidate_cost > 0:
                self.sol = candidate_sol
                self.cost = candidate_cost

                if history:
                    history_arr.append(self.cost)

            else:
                break

            if verbose > 0:
                print(
                    f"Iteration: {i +1} | Current solution cost: {candidate_cost} | Best solution cost: {self.cost}"
                )

        return ExecutionResult(sol=self.sol, cost=self.cost, history=history_arr)
