from scrape_web import scrape_page
from datetime import datetime as dt, timedelta
from Asset import Asset
from Order import Order
from Order_Book import Order_Book

class Portfolio():
    def __init__(self, asset_list, cash):
        self.asset_list = asset_list
        self.cash = cash
    
    def strat_ma(self, n_days):
        print('Executing a simple MA strategy...')
        self.order_book = Order_Book(self.cash)
        end_date = dt.now()
        start_date = end_date - timedelta(days=n_days)
        for asset in self.asset_list:
            df = scrape_page(asset.name, asset.ticker, start_date, end_date)
            ma = df['close'].rolling(len(df)).mean().iloc[-1]
            close = df['close'].iloc[-1]
            if ma > close and asset.position > 0:
                self.order_book.add_order(Order(asset, 'Sell', ma, asset.position))
            elif ma < close:
                self.order_book.add_order(Order(asset, 'Buy', ma, 1/float(df.std())))
        self.order_book.execute_order()
    
    def strat_ma_cross(self, short_dur, long_dur):
        print('Executing a MA cross-over strategy...')
        self.order_book = Order_Book(self.cash)
        end_date = dt.now()
        start_date = end_date - timedelta(days=long_dur)
        for asset in self.asset_list:
            df = scrape_page(asset.name, asset.ticker, start_date, end_date)
            short_start_date = end_date - timedelta(days=short_dur)
            _df = df[df.index >= short_start_date]
            ma_short =_df['close'].rolling(len(_df)).mean().iloc[-1]
            ma_long = df['close'].rolling(len(df)).mean().iloc[-1]
            close = df['close'].iloc[-1]
            if ma_short > ma_long and asset.position > 0:
                self.order_book.add_order(Order(asset, 'Sell', max(ma_short, close), asset.position))
            elif ma_short < ma_long:
                self.order_book.add_order(Order(asset, 'Buy', min(ma_short, close), 1/float(df.std())))
        self.order_book.execute_order()