from Asset import Asset
from Plotter import Plotter
from EuropeanCallOption import EuropeanCallOption
from MonteCarloPricer import MonteCarloPricer
from HoLee import HoLee


if __name__ == '__main__':
    print('Option pricing with MonteCarlo simulations')

    asset = Asset(mu=0.1, sigma=1, initial_price=100)
    sample_path = asset.simulate_ho_lee(time_horizon=10)
    plotter = Plotter(sample_path)
    plotter.plot()

    ho_lee = HoLee(asset)
    call = EuropeanCallOption(strike=100, time_horizon=10)
    mc_pricer = MonteCarloPricer(model=ho_lee,
                                 option=call,
                                 num_paths=100)
    print('Price of the European Option: ', mc_pricer.get_price())
