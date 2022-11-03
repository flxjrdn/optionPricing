import matplotlib.pyplot as plt
import numpy as np
from SamplePath import SamplePath


class Plotter:
    def __init__(self, sample_path: SamplePath):
        self.sample_path = sample_path

    def plot(self):
        x = np.arange(len(self.sample_path.price)) * self.sample_path.dt
        y = self.sample_path.price
        plt.plot(x, y)
        plt.xlabel('t')
        plt.ylabel('value')
        plt.show()
