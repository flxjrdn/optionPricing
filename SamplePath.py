import numpy as np


class SamplePath:
    def __init__(self, dt, price):
        self.dt = dt
        self.price = price

    def get_time_horizon(self):
        if self.price is None:
            return 0
        else:
            return (len(self.price) - 1) / self.dt
