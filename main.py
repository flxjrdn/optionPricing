from Asset import Asset
from Plotter import Plotter
from EuropeanCallOption import EuropeanCallOption
from MonteCarloPricer import MonteCarloPricer
from HoLee import HoLee
import BlackScholes

if __name__ == '__main__':
    print('Option pricing with MonteCarlo simulations')
    print(BlackScholes.get_option_price(initial_price=100, T=10, K=100, r=0, sigma=1))
    asset = Asset(mu=0.1, sigma=1, initial_price=100)
    sample_path = asset.simulate_ho_lee(time_horizon=10)
    plotter = Plotter(sample_path)
    plotter.plot()

    ho_lee = HoLee(asset)
    call = EuropeanCallOption(strike=100, time_horizon=10)
    mc_pricer = MonteCarloPricer(model=ho_lee,
                                 option=call,
                                 num_paths=1000)
    print('Price of the European Option: ', mc_pricer.get_price())


