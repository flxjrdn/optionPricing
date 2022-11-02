from BrownianMotion import BrownianMotion
from abc import ABC, abstractmethod


class ShortRateModel(ABC):
    def __init__(self):
        self.timesteps_per_unit_time = 1000
        self.dt = 1.0 / self.timesteps_per_unit_time
        self.bm = BrownianMotion(dt=self.dt,
                                 loc=0.0,
                                 scale=1.0)

    @abstractmethod
    def sample_path(self, time_horizon):
        pass
