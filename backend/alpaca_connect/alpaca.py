import yfinance as yf
import requests


def buy_order_alpaca(API_KEY, API_SECRET, ticker, price, quantity):
    
    url = 'https://paper-api.alpaca.markets/v2/orders'

    payload = {
        "symbol": ticker,
        "qty": quantity,
        "side": "buy",
        "type": "limit",
        "time_in_force": "day",
        "limit_price": price
    }
    headers = {
        "APCA-API-KEY-ID": API_KEY,
        "APCA-API-SECRET-KEY": API_SECRET,
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(f"Order response for {ticker}: {response.text}")
    

    pass


def port_buy(API_KEY, API_SECRET, upd_stock_list, buying_power):
    
    url = 'https://paper-api.alpaca.markets/v2/orders'

    ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
    }
    
    pricing = []
    

    weighting = buying_power/len(upd_stock_list)


    for i in upd_stock_list:
        stock = yf.Ticker(i)
        try:
            current_price = stock.info['currentPrice']
            pricing.append(current_price)
        except KeyError:
            print(f"Could not retrieve price for {i}.")
            pricing.append(None)




    portfolio_dict= dict(zip(upd_stock_list,pricing))
    print(portfolio_dict)




    for ticker, price in portfolio_dict.items():
        if price:
            quantity = weighting / price
            buy_order_alpaca(ticker, price, quantity)
        else:
            print(f"Skipping order for {ticker} due to missing price.")

    pass

    