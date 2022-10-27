import pandas as pd


class Asset:
    initial_price = 100

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        self.price = pd.DataFrame(data=[[0, self.initial_price],
                                        [1, self.initial_price * (1+mu)]],
                                  columns=['t', 'price'])

    def show_price(self):
        print(self.price.to_string(index=False))
