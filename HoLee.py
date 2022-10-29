import numpy as np
from ShortRateModel import ShortRateModel


class HoLee(ShortRateModel):
    def __init__(self, mu, sigma):
        super().__init__()
        self.mu = mu
        self.sigma = sigma

    # noinspection PyPep8Naming
    def simulate_price(self, time_horizon):
        dW = self.bm.get_dW(time_horizon * self.timesteps_per_unit_time)
        self.price = np.zeros(len(dW))
        return self.price
