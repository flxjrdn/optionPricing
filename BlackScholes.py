from scipy.stats import norm
import numpy as np


def get_option_price(initial_price, T, K, r, sigma):
    d1 = (1 / (sigma * np.sqrt(T))) * (np.log(initial_price / K) + (r + sigma**2 / 2) * T)
    d2 = d1 - sigma * np.sqrt(T)
    price = initial_price * norm.cdf(d1) - np.exp(-r*T) * K * norm.cdf(d2)
    return price
