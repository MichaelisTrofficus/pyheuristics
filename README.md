<p align="center">
    <img alt="Pyheuristics logo" src="img/logo.png" width=300 />
    <h1 align="center">PyHeuristics</h1>
    <h3 align="center">A toolkit for MetaHeuristics implemented in Python</h3>
</p>

---

**PyHeuristics** is a Metaheuristics toolkit,
which facilitates the use of various metaheuristic algorithms,
such as **Simulated Annealing** or **Ant Colony Optimization** among others.


### How to Install

TODO

### Basic Usage

Using the various abstractions of PyHeuristics,
it is really easy to solve an optimization problem.

Using the various abstractions of PyHeuristics,
it is really easy to solve an optimization problem.
For example, we will show how to find the maximum of
this expression using the Simulated Annealing algorithm.

```math
f(x) = x^3 - 60x^2 + 900x + 100
```

First of all import `SimulatedAnnealing` and `CoolingSchedule`. `CoolingSchedule`
is a class that regulated the temperature of the annealing process.

```python
from pyheuristics.trajectory.annealing.cooling_schedules import GeometricCoolingSchedule
from pyheuristics.trajectory.annealing.simulated_annealing import SimulatedAnnealing
```

Then, implement a class of the problem that must implement the `fn` and
the `move` methods.

```python
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
```

Finally, run the algorithm to search for the maximum value.

```python
cs = GeometricCoolingSchedule(initial_temp=25000.0, final_temp=2.5, alpha=0.9)
optim_problem = MaximizeSimpleFunction(init_sol="10011", cooling_schedule=cs)
execution_result = optim_problem.run()

print(execution_result.sol) # "01010"
print(execution_result.cost) # 4100
```
