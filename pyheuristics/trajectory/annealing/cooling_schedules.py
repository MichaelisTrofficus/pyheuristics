import abc
from abc import ABC


class CoolingSchedule(ABC):
    """
    Abstract Base Class for a Simulated Annealing Cooling Schedule
    """

    def __init__(self, initial_temp: float, final_temp: float):
        if initial_temp < 0 or final_temp < 0:
            raise ValueError("Temperatures must be positive magnitudes")
        self._temp = initial_temp
        self._final_temp = final_temp

    @property
    def temp(self):
        return self._temp

    @property
    def final_temp(self):
        return self._final_temp

    @abc.abstractmethod
    def update(self, *args, **kwargs) -> "CoolingSchedule":
        raise NotImplementedError(
            "Implement the `update` the cooling schedule method for "
        )


class LinearCoolingSchedule(CoolingSchedule):
    def __init__(self, initial_temp: float, final_temp: float, alpha: float = 10):
        super(LinearCoolingSchedule, self).__init__(initial_temp, final_temp)
        self.alpha = alpha

    def update(self):
        self._temp -= self.alpha
        return self


class GeometricCoolingSchedule(CoolingSchedule):
    def __init__(self, initial_temp: float, final_temp: float, alpha: float = 0.6):
        super(GeometricCoolingSchedule, self).__init__(initial_temp, final_temp)

        if alpha <= 0 or alpha >= 1:
            raise ValueError("`alpha` must be in the ]0, 1[ interval")
        self.alpha = alpha

    def update(self):
        self._temp *= self.alpha
        return self


class SlowDecreaseCoolingSchedule(CoolingSchedule):
    def __init__(self, initial_temp: float, final_temp: float, alpha: float = 0.01):
        super(SlowDecreaseCoolingSchedule, self).__init__(initial_temp, final_temp)
        self.alpha = alpha

    def update(self):
        self._temp = self._temp / (1 + self.alpha * self._temp)
        return self
