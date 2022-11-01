class EuropeanCallOption:
    def __init__(self, strike, time_horizon):
        self.strike = strike
        self.time_horizon = time_horizon

    def payoff(self, sample_path):
        return max(sample_path[-1] - self.strike, 0)
