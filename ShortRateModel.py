from BrownianMotion import BrownianMotion


class ShortRateModel:
    def __init__(self):
        self.timesteps_per_unit_time = 10
        self.dt = 1.0 / self.timesteps_per_unit_time
        self.bm = BrownianMotion(dt=self.dt,
                                 loc=0.0,
                                 scale=1.0)
        self.initial_price = 100
        self.price = None
