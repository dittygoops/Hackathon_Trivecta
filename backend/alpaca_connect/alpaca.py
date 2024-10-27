import yfinance as yf
import requests
import json

class StockOrder:
    def __init__(self, ticker, price, quantity):
        self.ticker = ticker
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"StockOrder(ticker={self.ticker}, price={self.price}, quantity={self.quantity})"


def buy_order_alpaca(API_KEY, API_SECRET, stock_order):
    
    url = 'https://paper-api.alpaca.markets/v2/orders'

    payload = {
        "symbol": stock_order.ticker,
        "qty": stock_order.quantity,
        "side": "buy",
        "type": "limit",
        "time_in_force": "day",
        "limit_price": stock_order.price
    }
    headers = {
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": API_SECRET,
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(f"Order response for {stock_order.ticker}: {response.text}")
    

def port_buy(API_KEY, API_SECRET, upd_stock_list, buying_power):
    
    pricing = []
    weighting = buying_power / len(upd_stock_list)
    stock_orders = []

    for ticker in upd_stock_list:
        stock = yf.Ticker(ticker)
        try:
            current_price = stock.info['currentPrice']
            pricing.append(current_price)
        except KeyError:
            print(f"Could not retrieve price for {ticker}.")
            pricing.append(None)

    portfolio_dict = dict(zip(upd_stock_list, pricing))
    print(portfolio_dict)

    for ticker, price in portfolio_dict.items():
        if price:
            quantity = weighting / price
            stock_order = StockOrder(ticker, price, quantity)
            stock_orders.append(stock_order)
            buy_order_alpaca(API_KEY, API_SECRET, stock_order)
        else:
            print(f"Skipping order for {ticker} due to missing price.")

    stock_orders_json = json.dumps([order.to_dict() for order in stock_orders], indent=4)
    return stock_orders_json