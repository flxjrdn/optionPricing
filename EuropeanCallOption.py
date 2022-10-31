class EuropeanCallOption:
    def __init__(self, strike):
        self.strike = strike

    def payoff(self, sample_path):
        return max(sample_path[-1] - self.strike, 0)
