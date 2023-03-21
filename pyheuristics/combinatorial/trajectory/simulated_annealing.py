from abc import ABC
from typing import Callable, Union

from pyheuristics.combinatorial.trajectory.base import TrajectoryMethod
from pyheuristics.execution_result import ExecutionResult


class SimulatedAnnealing(ABC, TrajectoryMethod):
    def __init__(self, init_sol, strategy: Union[Callable, str] = "first"):
        """
        Implementation of the LocalSearch algorithm

        Args:
            init_sol: The initial solution, i.e., the starting point of the trajectory. This parameter
                can be anything: a string, an array, a graph, etc. Basically, the data structure that best
                represents a solution to the problem.
            strategy: The type of strategy the algorithm follows when selecting a candidate from
                the set of neighbors. Currently, there are two strategies implemented:

                - 'best': Selecting the best candidate from all the candidates in the set of neighbors that is
                    also better than the best solution found so far.

                - 'first': selecting the first candidate that is better than the best solution found so far.

            However, this parameter also accepts a user-defined function as input. This function must have
            the same signature as the `pyheuristics.combinatorial.trajectory.utils.helpers.imp_best` and
            `pyheuristics.combinatorial.trajectory.utils.helpers.imp_first` functions.
        """
        self.init_sol = init_sol

        if strategy not in ["first", "best"] and type(strategy) != Callable:
            raise NotImplementedError(
                "improve_strategy must be one of ['first', 'best']"
            )

        self.strategy = strategy

    def run(self, max_iter: int = 1000, verbose=0, history=False) -> ExecutionResult:
        """
        Args:
            max_iter: Maximum iterations before stopping the algorithm
            verbose:
            history: pass
        """
        pass
