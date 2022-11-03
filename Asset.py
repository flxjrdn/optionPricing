from HoLee import HoLee


class Asset:

    def __init__(self, mu, sigma, initial_price=100):
        self.mu = mu
        self.sigma = sigma
        self.initial_price = initial_price

    def simulate_ho_lee(self, time_horizon):
        model = HoLee(self)
        return model.sample_path(time_horizon)
