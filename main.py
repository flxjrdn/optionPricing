from Asset import Asset


if __name__ == '__main__':
    print('Option pricing with MonteCarlo simulations')

    asset = Asset(mu=0.1, sigma=1)
    asset.simulate_price(time_horizon=5)
    asset.show_price()
