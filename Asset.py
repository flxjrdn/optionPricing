from HoLee import HoLee


class Asset:

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def simulate_ho_lee(self, time_horizon):
        model = HoLee(self.mu, self.sigma)
        return model.sample_path(time_horizon)
