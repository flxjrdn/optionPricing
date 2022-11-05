from Asset import Asset
from Plotter import Plotter
from EuropeanCallOption import EuropeanCallOption
from MonteCarloPricer import MonteCarloPricer
from HoLee import HoLee
import BlackScholes

if __name__ == '__main__':
    print('Option pricing with MonteCarlo simulations')
    T = 1
    K = 10
    sigma = 0.1
    initial_price = 100
    r = 0
    mu = 0
    print(BlackScholes.get_option_price(initial_price=initial_price, T=T, K=K, r=r, sigma=sigma))
    asset = Asset(mu=0, sigma=sigma, initial_price=initial_price)
    sample_path = asset.simulate_ho_lee(time_horizon=T)
    plotter = Plotter(sample_path)
    plotter.plot()

    ho_lee = HoLee(asset)
    call = EuropeanCallOption(strike=K, time_horizon=T)
    mc_pricer = MonteCarloPricer(model=ho_lee,
                                 option=call,
                                 num_paths=100,
                                 r=r)
    print('Price of the European Option: ', mc_pricer.get_price())


