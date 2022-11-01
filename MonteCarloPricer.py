from ShortRateModel import ShortRateModel
from EuropeanCallOption import EuropeanCallOption


class MonteCarloPricer:
    def __init__(self, option: EuropeanCallOption, model: ShortRateModel, num_paths=10):
        self.option = option
        self.model = model
        self.num_paths = num_paths

    def get_price(self):
        price = 0

        for i in range(self.num_paths):
            sample_path = self.model.sample_path(time_horizon)
            print(self.option.payoff(sample_path))
            price += self.option.payoff(sample_path)

        return price / self.num_paths
