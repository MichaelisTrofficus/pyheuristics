from copy import deepcopy

from pyheuristics.trajectory import LocalSearch
from pyheuristics.utils.search_strategies import best_strategy


def test_local_search():
    """
    Solve an instance of Knapsack problem
    """

    class KnapsackProblem(LocalSearch):
        """
        Implementation of Knapsack problem as in Wikipedia example: https://en.wikipedia.org/wiki/Knapsack_problem
        """

        # Order list of values according to weight
        LIST_OF_VALUES = [1, 2, 2, 10, 4]
        LIST_OF_WEIGHTS = [1, 1, 2, 4, 12]
        TOTAL_CAPACITY = 15

        # We treat each solution as an array of booleans. 1 means the object is inside the knapsack, 0 that it isn't

        def fn(self, sol):
            """
            Computes the total value of all the objects inside the knapsack
            """
            total_value = 0
            for index, in_bag in enumerate(sol):
                total_value += self.LIST_OF_VALUES[index] * in_bag
            return -total_value

        def get_total_weight(self, sol):
            total_weight = 0
            for index, in_bag in enumerate(sol):
                total_weight += self.LIST_OF_WEIGHTS[index] * in_bag
            return total_weight

        def move(self):
            """
            For example, perform a permutation in each element of the array
            """

            # We will select a set of neighbors from the current solution / state

            neighbors = []

            for i in range(len(self.sol)):
                neighbor = deepcopy(self.sol)
                neighbor[i] = 0 if self.sol[i] else 1

                if self.get_total_weight(neighbor) <= self.TOTAL_CAPACITY:
                    neighbors.append(neighbor)

            # Now, simply select the best neighbor using a `best` strategy
            return best_strategy(self.fn, self.sol, self.cost, neighbors)

    init_sol = [1, 1, 0, 0, 0]
    knapsack = KnapsackProblem(init_sol=init_sol)

    # The optimal result is picking the two 1kg blocks, the 2 kg block and the 4 kg block.
    execution_result = knapsack.run(20)
    assert execution_result.sol == [1, 1, 1, 1, 0]
    assert execution_result.cost == -15
