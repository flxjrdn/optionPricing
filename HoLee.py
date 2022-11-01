import numpy as np
from ShortRateModel import ShortRateModel


class HoLee(ShortRateModel):
    def __init__(self, asset):
        super().__init__()
        self.asset = asset

    # noinspection PyPep8Naming
    def sample_path(self, time_horizon):
        dW = self.bm.get_dW(time_horizon * self.timesteps_per_unit_time)
        self.price = np.zeros(len(dW) + 1)
        self.price[0] = self.initial_price
        for i, dWt in enumerate(dW):
            self.price[i+1] = self.price[i] + self.asset.mu * self.dt + self.asset.sigma * dWt
        return self.price
