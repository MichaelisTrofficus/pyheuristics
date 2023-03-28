from abc import ABC
from typing import Any
import math
import random

from pyheuristics.trajectory.base import TrajectoryMethod
from pyheuristics.execution_result import ExecutionResult
from pyheuristics.trajectory.annealing.cooling_schedules import CoolingSchedule


class HomogeneousSimulatedAnnealing(TrajectoryMethod, ABC):
    def __init__(
        self,
        init_sol: Any,
        t_min: float,
        t_max: float,
        cooling_schedule: CoolingSchedule,
        max_iter_per_temp: int = 100,
    ):
        """
        Implementation of the LocalSearch algorithm

        Args:
            init_sol: The initial solution, i.e., the starting point of the trajectory. This parameter
                can be anything: a string, an array, a graph, etc. Basically, the data structure that best
                represents a solution to the problem.

            t_min: Minimum temperature

            t_max: Maximum temperature

            cooling_schedule: A cooling schedule

            max_iter_per_temp: Number of iterations per each temperature
        """
        self.sol, self.cost = self._get_sol_and_cost(init_sol)

        self.t_min = t_min
        self.t_max = t_max
        self.cooling_schedule = cooling_schedule
        self.max_iter = max
        self.max_iter_per_temp = max_iter_per_temp

        self.current_temp = t_max

    def run(self, max_iter: int = 1000, verbose=0, history=False) -> ExecutionResult:
        """
        Args:
            max_iter: Maximum iterations before stopping the algorithm
            verbose:
            history: pass
        """
        best_sol = self.sol
        best_cost = self.cost
        history_arr = [self.cost]

        while self.current_temp >= self.t_min:
            for _ in range(self.max_iter_per_temp):
                neighbor, neighbor_E = self.__getattribute__(self.move())
                dE = self.cost - self.fn(neighbor)

                if dE > 0:
                    self.sol = neighbor
                    self.cost = neighbor_E
                    history_arr.append(neighbor_E)
                else:
                    if random.uniform(0, 1) < math.exp(-dE / self.current_temp):
                        self.sol = neighbor
                        self.cost = neighbor_E
                        history_arr.append(neighbor_E)

                if self.cost < best_cost:
                    best_sol = self.cost
                    best_cost = self.cost

            self.current_temp = self.cooling_schedule.update().temp

        return ExecutionResult(sol=best_sol, cost=best_cost, history=history_arr)


class InHomogeneousSimulatedAnnealing(TrajectoryMethod, ABC):
    def __init__(
        self,
        init_sol: Any,
        t_min: float,
        t_max: float,
        cooling_schedule: CoolingSchedule,
    ):
        """
        Implementation of the LocalSearch algorithm

        Args:
            init_sol: The initial solution, i.e., the starting point of the trajectory. This parameter
                can be anything: a string, an array, a graph, etc. Basically, the data structure that best
                represents a solution to the problem.

            t_min: Minimum temperature

            t_max: Maximum temperature

            cooling_schedule: A cooling schedule
        """
        self.sol, self.cost = self._get_sol_and_cost(init_sol)

        self.t_min = t_min
        self.t_max = t_max
        self.cooling_schedule = cooling_schedule
        self.max_iter = max

        self.current_temp = t_max

    def run(self, max_iter: int = 1000, verbose=0, history=False) -> ExecutionResult:
        """
        Args:
            max_iter: Maximum iterations before stopping the algorithm
            verbose:
            history: pass
        """
        best_sol = self.sol
        best_cost = self.cost
        history_arr = [self.cost]

        while self.current_temp >= self.t_min:
            neighbor, neighbor_E = self.__getattribute__(self.move())
            dE = self.cost - self.fn(neighbor)

            if dE > 0:
                self.sol = neighbor
                self.cost = neighbor_E
                history_arr.append(neighbor_E)
            else:
                if random.uniform(0, 1) < math.exp(-dE / self.current_temp):
                    self.sol = neighbor
                    self.cost = neighbor_E
                    history_arr.append(neighbor_E)

            if self.cost < best_cost:
                best_sol = self.cost
                best_cost = self.cost

            self.current_temp = self.cooling_schedule.update().temp

        return ExecutionResult(sol=best_sol, cost=best_cost, history=history_arr)
