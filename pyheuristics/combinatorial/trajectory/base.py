import abc
from abc import ABC
from typing import Any, Tuple
from pyheuristics.execution_result import ExecutionResult


class TrajectoryMethod(ABC):
    """
    Abstract Base Class for Trajectory Methods.
    """

    def _get_sol_and_cost(self, sol: Any) -> Tuple[Any, float]:
        """
        A tuple where its first element is the solution provided and the second element
        its cost
        """
        return sol, self.fn(sol)

    @abc.abstractmethod
    def fn(self, sol: Any) -> float:
        """
        # TODO: Improve this docstring pls
        The objective function to be minimized. Remember that all `pyheuristics` algorithms
        will try to minimize the objective function. So, in case you are trying to find the maximum,
        simply negate the result.

        Args:
            sol: The solution to be evaluated by the objective function

        Examples:
            pass

        Returns:
            A float representing the evaluation of `sol` by the objective function
        """
        raise NotImplementedError

    @abc.abstractmethod
    def move(self) -> Any:
        """
        This method represents a single move in the search space. Since we are dealing with trajectory methods,
        the algorithm will be drawing a "trajectory" in the search space, and each point of this trajectory is
        reached by means of a move operation.

        Returns:
            It returns a new point of the trajectory.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def run(self, **kwargs) -> ExecutionResult:
        """
        The main method for running the different algorithms. It must return an `ExecutionResult` dataclass,
        since we will be gathering all metadata from the execution in these type of objects.
        """
        raise NotImplementedError
