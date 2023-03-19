import abc
from abc import ABCMeta
from typing import Callable, Union
from pyheuristics.combinatorial.trajectory.utils.helpers import imp_best, imp_first
from pyheuristics.execution_result import ExecutionResult


class LocalSearch(metaclass=ABCMeta):
    def __init__(self, init_sol, improve_strategy: Union[Callable, str] = "first"):
        """
        Implementation of the LocalSearch algorithm

        Args:
            init_sol: The initial solution, i.e., the starting point of the trajectory. This parameter
                can be anything: a string, an array, a graph, etc. Basically, the data structure that best
                represents a solution to the problem.
            improve_strategy: The type of strategy the algorithm follows when selecting a candidate from
                the set of neighbors. Currently, there are two strategies implemented:

                - 'best': Selecting the best candidate from all the candidates in the set of neighbors that is
                    also better than the best solution found so far.

                - 'first': selecting the first candidate that is better than the best solution found so far.

            However, this parameter also accepts a user-defined function as input. This function must have
            the same signature as the `pyheuristics.combinatorial.trajectory.utils.helpers.imp_best` and
            `pyheuristics.combinatorial.trajectory.utils.helpers.imp_first` functions.
        """
        self.init_sol = init_sol

        if (
            improve_strategy not in ["first", "best"]
            and type(improve_strategy) != Callable
        ):
            raise NotImplementedError(
                "improve_strategy must be one of ['first', 'best']"
            )

        self.improve_strategy = improve_strategy

    def improve(self, curr_sol, curr_cost, neighbors: list):
        if self.improve_strategy == "first":
            return imp_first(self.objective_fn, curr_sol, curr_cost, neighbors)
        elif self.improve_strategy == "best":
            return imp_best(self.objective_fn, curr_sol, curr_cost, neighbors)
        else:
            # User-defined improve strategies will be called here
            return self.improve_strategy(
                self.objective_fn, curr_sol, curr_cost, neighbors
            )

    @abc.abstractmethod
    def objective_fn(self, sol):
        raise NotImplementedError

    @abc.abstractmethod
    def get_neighbors(self, sol):
        raise NotImplementedError

    def search(self, max_iter: int = 1000, verbose=0, history=False) -> ExecutionResult:
        """
        Args:
            max_iter: Maximum iterations before stopping the algorithm
            verbose:
            history: pass
        """
        it = 0
        history_arr = []
        curr_sol = self.init_sol
        curr_cost = self.objective_fn(curr_sol)

        while it <= max_iter:
            candidate_sol, candidate_cost = self.improve(
                curr_sol, curr_cost, self.get_neighbors(curr_sol)
            )
            if curr_cost - candidate_cost > 0:
                curr_sol = candidate_sol
                curr_cost = candidate_cost
                if history:
                    history_arr.append(curr_cost)
            else:
                break

            if verbose > 0:
                print(
                    f"Current solution cost: {candidate_cost} | Best solution cost: {curr_cost}"
                )

            it += 1
        return ExecutionResult(sol=curr_sol, cost=curr_cost, history=history_arr)
