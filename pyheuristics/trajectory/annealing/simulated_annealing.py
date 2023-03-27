from abc import ABC
from typing import Any

from pyheuristics.trajectory.base import TrajectoryMethod
from pyheuristics.execution_result import ExecutionResult
from pyheuristics.trajectory.annealing.cooling_schedules import BaseCoolingSchedule


class SimulatedAnnealing(TrajectoryMethod, ABC):
    def __init__(
        self,
        init_sol: Any,
        t_min: float,
        t_max: float,
        cooling_schedule: BaseCoolingSchedule,
    ):
        """
        Implementation of the LocalSearch algorithm

        Args:
            init_sol: The initial solution, i.e., the starting point of the trajectory. This parameter
                can be anything: a string, an array, a graph, etc. Basically, the data structure that best
                represents a solution to the problem.

            t_min: Minimum temperature

            t_max: Maximum temperature

        """
        self.init_sol = init_sol
        self.t_min = t_min
        self.t_max = t_max

    def run(self, max_iter: int = 1000, verbose=0, history=False) -> ExecutionResult:
        """
        Args:
            max_iter: Maximum iterations before stopping the algorithm
            verbose:
            history: pass
        """
        pass
