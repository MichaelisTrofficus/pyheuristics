from typing import Callable, Any, List


def first_strategy(fn: Callable, sol: Any, cost: float, neighbors: List[Any]) -> Any:
    """
    Selects the first candidate that is better than the best solution found so far.

    Args:
        fn: The objective function of the optimization problem
        sol: The current solution
        cost: The current solution's cost. We are passing this to avoid another recalculation.
        neighbors: The list of neighbors

    Returns:
        A solution
    """
    for neighbor in neighbors:
        if fn(neighbor) < cost:
            return neighbor
    return sol


def best_strategy(fn: Callable, sol: Any, cost: Any, neighbors: List[Any]) -> Any:
    """
    Selects the best candidate from all the candidates in the set of neighbors that is
    also better than the best solution found so far.

    Args:
        fn: The objective function of the optimization problem
        sol: The current solution
        cost: The current solution's cost
        neighbors: The list of neighbors

    Returns:
        A solution
    """
    best_sol = sol
    best_cost = cost

    for neighbor in neighbors:
        if fn(neighbor) < best_cost:
            best_sol = neighbor
            best_cost = fn(neighbor)
    return best_sol
