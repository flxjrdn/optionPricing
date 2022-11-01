from Asset import Asset
from Plotter import Plotter
from EuropeanCallOption import EuropeanCallOption
from MonteCarloPricer import MonteCarloPricer
from HoLee import HoLee


if __name__ == '__main__':
    print('Option pricing with MonteCarlo simulations')

    asset = Asset(mu=0.1, sigma=1)
    # asset.simulate_ho_lee(time_horizon=5)

    ho_lee = HoLee()

    plotter = Plotter(asset)
    # plotter.plot()

    call = EuropeanCallOption(strike=100)
    mc_pricer = MonteCarloPricer(option=call,
                                 model=ho_lee,
                                 num_paths=10)
