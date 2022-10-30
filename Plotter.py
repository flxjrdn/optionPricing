import matplotlib.pyplot as plt
from Asset import Asset


class Plotter:
    def __init__(self, asset: Asset):
        self.asset = asset

    def plot(self):
        plt.plot(self.asset.price_history)
        plt.show()
