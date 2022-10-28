from BrownianMotion import BrownianMotion


class ShortRateModel:
    def __init__(self):
        self.price = None
        self.bm = BrownianMotion()
        self.dW = self.bm.get_dW()
