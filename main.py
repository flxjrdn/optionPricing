from Asset import Asset


if __name__ == '__main__':
    print('Option pricing with MonteCarlo simulations')

    asset = Asset(mu=0.1, sigma=1)
    asset.show_price()
