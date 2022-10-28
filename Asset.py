from HoLee import HoLee


class Asset:

    def __init__(self, mu, sigma):
        self.price_history = None
        self.mu = mu
        self.sigma = sigma
        self.simulate_price()

    def simulate_price(self):
        model = HoLee(self.mu, self.sigma)
        self.price_history = model.simulate_price()

    def show_price(self):
        print(self.price_history.to_string(index=False))
