from Asset import Asset
from Plotter import Plotter


if __name__ == '__main__':
    print('Option pricing with MonteCarlo simulations')

    asset = Asset(mu=0.1, sigma=1)
    asset.simulate_ho_lee(time_horizon=5)

    plotter = Plotter(asset)
    plotter.plot()
