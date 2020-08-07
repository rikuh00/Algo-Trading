from datetime import datetime as dt, timedelta

class Asset:
    def __init__(self, name, ticker, position):
        self.name = name
        self.ticker = ticker
        self.position = position
