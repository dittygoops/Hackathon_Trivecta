import yfinance as yf
import numpy as np
import pandas as pd

def calculate_risk_score(ticker):
    try:
        al_score = round(get_AL_ratio_score(ticker), 2)
        if al_score == 0:
            al_score += 27.5
            
        rsi = calculate_rsi(ticker, 14)
        rsi = 0 if rsi is None else rsi

        coeff_variation_ = coeff_variation(ticker)
        coeff_variation_ = coeff_variation_ / 3.5 if coeff_variation_ is not None else 0

        beta = calculate_beta(ticker)
        beta = round((beta - 1) * 12.5) if beta is not None else 0

        # Weighted total score
        risk_score = (coeff_variation_ + al_score + beta + rsi)    
        return abs(round(risk_score, 2))
    except Exception as e:
        print(f"Error calculating risk score for {ticker}: {e}")
        return 75.46
    

def get_AL_ratio_score(ticker):
    try:
        ticker_data = yf.Ticker(ticker)
        balance_sheet = ticker_data.balance_sheet

        if balance_sheet.empty:
            print(f"Warning: Balance sheet data for {ticker} is empty.")
            return 35  # Average score if data is unavailable

        total_assets = balance_sheet.loc["Total Assets"].iloc[0]
        total_liabilities = balance_sheet.loc["Total Liabilities Net Minority Interest"].iloc[0]
        al_ratio = total_assets / total_liabilities if total_liabilities else 0

        score = min(100, max(0, (al_ratio - 1) * 5))
        return score
    except Exception as e:
        print(f"Error calculating AL ratio score for {ticker}: {e}")
        return 35  # Average score if data is unavailable
    
def calculate_beta(stock_ticker, benchmark_ticker='^GSPC', period='1y'):
    try:
        stock_data = yf.Ticker(stock_ticker).history(period=period)
        benchmark_data = yf.Ticker(benchmark_ticker).history(period=period)

        if stock_data.empty or benchmark_data.empty:
            print(f"Warning: Stock or benchmark data for {stock_ticker} is empty.")
            return None

        stock_returns = stock_data['Close'].pct_change().dropna()
        benchmark_returns = benchmark_data['Close'].pct_change().dropna()

        combined_returns = pd.concat([stock_returns, benchmark_returns], axis=1)
        combined_returns.columns = ['Stock', 'Benchmark']
        combined_returns.dropna(inplace=True)

        if len(combined_returns) < 2:
            print(f"Warning: Not enough data points to calculate beta for {stock_ticker}.")
            return None

        covariance = np.cov(combined_returns['Stock'], combined_returns['Benchmark'])[0][1]
        benchmark_variance = np.var(combined_returns['Benchmark'])

        if benchmark_variance == 0:
            print(f"Warning: Benchmark variance is zero for {benchmark_ticker}.")
            return None

        beta = covariance / benchmark_variance
        return round(beta, 4)
    except Exception as e:
        print(f"Error calculating beta for {stock_ticker}: {e}")
        return None

def calculate_rsi(ticker, period=14):
    try:
        ticker_data = yf.Ticker(ticker)
        hist = ticker_data.history(period="1y")
        
        if hist.empty:
            print(f"Warning: Historical data for {ticker} is empty.")
            return None
            
        delta = hist['Close'].diff()
        gains = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        losses = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gains / losses if losses.mean() != 0 else 0
        rsi = 100 - (100 / (1 + rs))

        return rsi.iloc[-1] if not rsi.isnull().all() else None
    except Exception as e:
        print(f"Error calculating RSI for {ticker}: {e}")
        return None

def coeff_variation(ticker):
    try:
        ticker_data = yf.Ticker(ticker)
        hist = ticker_data.history(period="5y")
        
        if hist.empty:
            print(f"Warning: Historical data for {ticker} is empty.")
            return None
        
        hist['Returns'] = hist['Close'].pct_change().dropna()
        average_return = hist['Returns'].mean()
        std_dev = hist['Returns'].std()
        
        if average_return != 0:
            cv = std_dev / average_return
            return abs(round(cv, 4))
        else:
            print(f"Warning: Average return for {ticker} is zero.")
            return None
    except Exception as e:
        print(f"Error calculating coefficient of variation for {ticker}: {e}")
        return None
