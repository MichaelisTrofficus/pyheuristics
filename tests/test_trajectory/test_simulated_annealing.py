import random
from typing import Any

from pyheuristics.trajectory.annealing.cooling_schedules import (
    LinearCoolingSchedule,
    GeometricCoolingSchedule,
    SlowDecreaseCoolingSchedule,
)

from pyheuristics.trajectory.annealing.simulated_annealing import SimulatedAnnealing


def test_linear_cooling_schedule():
    cs = LinearCoolingSchedule(initial_temp=100, final_temp=0, alpha=10)
    assert cs.temp == 100
    assert cs.final_temp == 0
    assert cs.alpha == 10

    cs.update()
    assert cs.temp == 90


def test_geometric_cooling_schedule():
    cs = GeometricCoolingSchedule(initial_temp=100, final_temp=0, alpha=0.7)
    assert cs.temp == 100
    assert cs.final_temp == 0
    assert cs.alpha == 0.7

    cs.update()
    assert cs.temp == 70


def test_slow_decrease_cooling_schedule():
    cs = SlowDecreaseCoolingSchedule(initial_temp=100, final_temp=0, alpha=0.01)
    assert cs.temp == 100
    assert cs.final_temp == 0
    assert cs.alpha == 0.01

    cs.update()
    assert cs.temp == 100 / (1 + 0.01 * 100)


def test_simulated_annealing():
    """
    Maximize the continuous function:
        f(x) = x^3 - 60x^2 + 900x + 100

    A solution x will be represented as a string of 5 bits. The neighborhood consists in flipping
    randomly a bit. The global maximum of this function is:
        01010 (x=10, f(x) = 4100)

    The initial solution is 10011 (x=19, f(x) = 2399)
    """

    random.seed(312)

    class MaximizeSimpleFunction(SimulatedAnnealing):
        def fn(self, sol: Any) -> float:
            binary_to_decimal = int(sol, 2)
            return -(
                binary_to_decimal**3
                - 60 * (binary_to_decimal**2)
                + 900 * binary_to_decimal
                + 100
            )

        def move(self) -> Any:
            bit_to_flip = random.randint(0, 4)
            _list = list(self.sol)

            if self.sol[bit_to_flip] == "1":
                _list[bit_to_flip] = "0"
            else:
                _list[bit_to_flip] = "1"

            return "".join(_list)

    cs = GeometricCoolingSchedule(initial_temp=25000.0, final_temp=2.5, alpha=0.9)
    optim_problem = MaximizeSimpleFunction(init_sol="10011", cooling_schedule=cs)
    execution_result = optim_problem.run()

    assert execution_result.sol == "01010"
    assert execution_result.cost == -4100
