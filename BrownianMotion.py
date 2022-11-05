import numpy as np


class BrownianMotion:
    def __init__(self, dt):
        self.loc = 0.0
        self.scale = 1.0
        self.dt = dt

    # noinspection PyPep8Naming
    def get_dW(self, num):
        norm = np.random.normal(loc=self.loc,
                                scale=self.scale,
                                size=num)
        sqrt_dt = np.sqrt(self.dt)
        dW = norm * sqrt_dt
        return dW
