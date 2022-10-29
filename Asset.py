from HoLee import HoLee


class Asset:

    def __init__(self, mu, sigma):
        self.price_history = None
        self.mu = mu
        self.sigma = sigma

    def simulate_price(self, time_horizon):
        model = HoLee(self.mu, self.sigma)
        self.price_history = model.simulate_price(time_horizon)

    def show_price(self):
        print(self.price_history)
