from dataclasses import dataclass
from typing import Any, List


@dataclass
class ExecutionResult:
    """
    This dataclass is used to collect information about the execution of the various algorithms.
    It exposes information such as the best solution, the value of the objective function,
    history of the values of the objective function during the search process, etc.
    """

    sol: Any
    cost: float
    history: List[float]
