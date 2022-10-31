from Asset import Asset
from Plotter import Plotter
from EuropeanCallOption import EuropeanCallOption


if __name__ == '__main__':
    print('Option pricing with MonteCarlo simulations')

    asset = Asset(mu=0.1, sigma=1)
    asset.simulate_ho_lee(time_horizon=5)

    plotter = Plotter(asset)
    # plotter.plot()

    call = EuropeanCallOption(strike=100)

    print(asset.price_history[-1])
    print(call.payoff(asset.price_history))
