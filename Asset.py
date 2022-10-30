from HoLee import HoLee
from ShortRateModel import ShortRateModel


class Asset:

    def __init__(self, mu, sigma):
        self.price_history = None
        self.mu = mu
        self.sigma = sigma
        self.model = ShortRateModel

    def simulate_ho_lee(self, time_horizon):
        self.model = HoLee(self.mu, self.sigma)
        self.price_history = self.model.simulate_price(time_horizon)