class Order():
    def __init__(self, asset, signal, price, qty):
        self.asset = asset
        self.signal = signal
        self.price = price
        self.qty = qty #actual qty for sell, fraction of cash for buy