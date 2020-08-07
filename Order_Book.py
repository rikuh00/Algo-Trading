class Order_Book():
    def __init__(self, cash):
        self.buy_book = []
        self.sell_book = []
        self.cash = cash

    def add_order(self, order):
        if order.signal == 'Buy':
            self.buy_book.append(order)
        elif order.signal == 'Sell':
            self.sell_book.append(order)
    
    def execute_order(self):
        sum_weight = sum([order.qty for order in self.buy_book])
        for order in self.buy_book:
            avail_cash = (order.qty / sum_weight) * self.cash
            order.qty = avail_cash // order.price
            print('{}: Buy {:.0f} shares at ${:,.2f}'.format(order.asset.name, order.qty, order.price))
        
        for order in self.sell_book:
            print('{}: Sell {:.0f} shares at ${:,.2f}'.format(order.asset.name, order.qty, order.price))
        print()