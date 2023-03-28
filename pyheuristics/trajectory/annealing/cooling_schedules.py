import abc
from abc import ABC


class CoolingSchedule(ABC):
    """
    Abstract Base Class for a Simulated Annealing Cooling Schedule
    """

    def __init__(self, initial_temp: float):
        if initial_temp < 0:
            raise ValueError("Temperature must be a positive magnitude")
        self._temp = initial_temp

    @property
    def temp(self):
        return self._temp

    @abc.abstractmethod
    def update(self, *args, **kwargs) -> "CoolingSchedule":
        raise NotImplementedError(
            "Implement the `update` the cooling schedule method for "
        )


class LinearCoolingSchedule(CoolingSchedule):
    def __init__(self, initial_temp: float, alpha: float):
        super(LinearCoolingSchedule, self).__init__(initial_temp)
        self.alpha = alpha

    def update(self):
        self._temp -= self.alpha
        return self


class GeometricCoolingSchedule(CoolingSchedule):
    def __init__(self, initial_temp: float, alpha: float = 0.6):
        super(GeometricCoolingSchedule, self).__init__(initial_temp)

        if alpha <= 0 or alpha >= 1:
            raise ValueError("`alpha` must be in the ]0, 1[ interval")
        self.alpha = alpha

    def update(self):
        self._temp *= self.alpha
        return self


class SlowDecreaseCoolingSchedule(CoolingSchedule):
    def __init__(self, initial_temp: float, alpha: float):
        super(SlowDecreaseCoolingSchedule, self).__init__(initial_temp)
        self.alpha = alpha

    def update(self):
        self._temp = self._temp / (1 + self.alpha * self._temp)
        return self
