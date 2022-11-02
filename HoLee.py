import numpy as np
from ShortRateModel import ShortRateModel
from SamplePath import SamplePath


class HoLee(ShortRateModel):
    def __init__(self, asset):
        super().__init__()
        self.asset = asset

    # noinspection PyPep8Naming
    def sample_path(self, time_horizon):
        timesteps = time_horizon * self.timesteps_per_unit_time
        dW = self.bm.get_dW(timesteps)
        price = np.zeros(timesteps + 1)
        price[0] = self.asset.initial_price
        for i, dWt in enumerate(dW):
            price[i+1] = price[i] + self.asset.mu * self.dt + self.asset.sigma * dWt
        sample_path = SamplePath(dt=self.dt, price=price)
        return sample_path
