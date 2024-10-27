import yfinance as yf
import numpy as np
import pandas as pd

def calculate_risk_score(ticker):
        
        al_score = round(get_AL_ratio_score(ticker),2)
        if al_score == 0:
            al_score += 27.5
        
        
        rsi = 0
        rsi = calculate_rsi(ticker, 14)
        
        if(rsi > 75):
            rsi = 5.5
        elif(rsi<45):
            rsi = -5.5
        else:
            rsi = 0
        coeff_variation_ = coeff_variation(ticker)/3.5
        beta = round(((calculate_beta(ticker))-1)*12.5)
        # print('coeff: '+str(coeff_variation_))
        # print('al ratio: '+str(al_score))
        # print('beta: '+str(beta))
        # print('rsi:' + str(rsi))
    

        # Weighted total score
        risk_score = (coeff_variation_+al_score+beta+rsi)    

        return abs(round(risk_score, 2))
    

def get_AL_ratio_score(ticker):
    ticker = yf.Ticker(ticker)
    try:
        balance_sheet = ticker.balance_sheet
        total_assets = balance_sheet.loc["Total Assets"].iloc[0]  # Use .iloc for positional indexing
        total_liabilities = balance_sheet.loc["Total Liabilities Net Minority Interest"].iloc[0]  # Use .iloc for positional indexing
        al_ratio = total_assets / total_liabilities if total_liabilities else 0

        # Score AL ratio: higher ratio is lower risk
        score = min(100, max(0, (al_ratio - 1) * 5))
        return score
    except Exception as e:
        print(f"Error calculating AL ratio score: {e}")
        return 35  # Average score if data is unavailable
    
def calculate_beta(stock_ticker, benchmark_ticker='^GSPC', period='1y'):
    # Fetch historical price data for both the stock and benchmark
    try:
        stock_data = yf.Ticker(stock_ticker).history(period=period)
        benchmark_data = yf.Ticker(benchmark_ticker).history(period=period)

        # Calculate daily returns
        stock_returns = stock_data['Close'].pct_change().dropna()
        benchmark_returns = benchmark_data['Close'].pct_change().dropna()

        combined_returns = pd.concat([stock_returns, benchmark_returns], axis=1)
        combined_returns.columns = ['Stock', 'Benchmark']
        combined_returns.dropna(inplace=True)  # Drop any rows with NaN values

        # Perform linear regression to find beta
        covariance = np.cov(combined_returns['Stock'], combined_returns['Benchmark'])[0][1]
        benchmark_variance = np.var(combined_returns['Benchmark'])

        beta = covariance / benchmark_variance

        return round(beta, 4)
    except Exception as e:
        print(f"Error calculating beta for {stock_ticker}: {e}")
        return None



def calculate_rsi(ticker, period=14):
    # Fetch historical price data
    try:
        ticker_data = yf.Ticker(ticker)
        hist = ticker_data.history(period="1y")  # Get 1 year of historical data
        
        # Calculate daily returns
        delta = hist['Close'].diff()
        
        # Separate gains and losses
        gains = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        losses = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        # Calculate RS
        rs = gains / losses
        
        # Calculate RSI
        rsi = 100 - (100 / (1 + rs))
        
        return rsi.iloc[-1]  # Return the latest RSI value
    except Exception as e:
        print(f"Error calculating RSI for {ticker}: {e}")
        return None

def coeff_variation(ticker):
    # Pull the last 5 years of price data
    try:
        ticker_data = yf.Ticker(ticker)
        hist = ticker_data.history(period="5y")  # Get 5 years of historical data
        # Calculate daily returns
        hist['Returns'] = hist['Close'].pct_change().dropna()
        
        # Calculate the average return
        average_return = hist['Returns'].mean()
        
        # Calculate the standard deviation of returns
        std_dev = hist['Returns'].std()
        
        # Calculate the coefficient of variation
        if average_return != 0:  # Prevent division by zero
            cv = std_dev / average_return
            return abs(round(cv, 4)) # Round for better readability
        else:
            return None  # Return None if average return is zero
    except Exception as e:
        print(f"Error calculating coefficient of variation for {ticker}: {e}")
        return None