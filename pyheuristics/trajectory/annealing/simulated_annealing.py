from abc import ABC
from typing import Any
import math
import random

from pyheuristics.trajectory.base import TrajectoryMethod
from pyheuristics.execution_result import ExecutionResult
from pyheuristics.trajectory.annealing.cooling_schedules import CoolingSchedule


class SimulatedAnnealing(TrajectoryMethod, ABC):
    def __init__(
        self,
        init_sol: Any,
        cooling_schedule: CoolingSchedule,
    ):
        """
        Implementation of the InHomogeneous Simulated Annealing

        Args:
            init_sol: The initial solution, i.e., the starting point of the trajectory. This parameter
                can be anything: a string, an array, a graph, etc. Basically, the data structure that best
                represents a solution to the problem.

            cooling_schedule: A cooling schedule

        """
        self.sol, self.cost = self._get_sol_and_cost(init_sol)
        self.cooling_schedule = cooling_schedule

        self.current_temp = self.cooling_schedule.temp
        self.final_temp = self.cooling_schedule.final_temp

    def run(self, verbose=0, history=False) -> ExecutionResult:
        """
        Args:
            verbose:
            history: pass
        """
        best_sol = self.sol
        best_cost = self.cost
        history_arr = [self.cost]

        while self.current_temp >= self.final_temp:
            neighbor, neighbor_E = self._get_sol_and_cost(self.move())
            dE = self.cost - self.fn(neighbor)

            if dE >= 0:
                self.sol = neighbor
                self.cost = neighbor_E
                history_arr.append(neighbor_E)
            else:
                if random.uniform(0, 1) < math.exp(dE / self.current_temp):
                    self.sol = neighbor
                    self.cost = neighbor_E
                    history_arr.append(neighbor_E)

            if self.cost < best_cost:
                best_sol = self.sol
                best_cost = self.cost

            self.current_temp = self.cooling_schedule.update().temp

        return ExecutionResult(sol=best_sol, cost=best_cost, history=history_arr)
