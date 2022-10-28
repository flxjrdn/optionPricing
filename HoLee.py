import pandas as pd
from ShortRateModel import ShortRateModel


class HoLee(ShortRateModel):
    def __init__(self, mu, sigma):
        self.initial_price = 100
        self.mu = mu
        self.sigma = sigma
        self.simulate_price()

    def simulate_price(self):
        self.price = pd.DataFrame(data=[[0, self.initial_price],
                                        [1, self.initial_price * (1 + self.mu)]],
                                  columns=['t', 'price'])
        return self.price
