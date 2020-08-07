from Asset import Asset
from Portfolio import Portfolio
if __name__ == '__main__':
    vgro = Asset('VGRO', 'VGRO.TO', 27)
    vbal = Asset('VBAL', 'VBAL.TO', 0)
    vre = Asset('VRE', 'VRE.TO', 0)
    asset_list = [vgro, vbal, vre]
    portfolio = Portfolio(asset_list, cash=150)
    portfolio.strat_ma(40)
    portfolio.strat_ma_cross(40, 100)