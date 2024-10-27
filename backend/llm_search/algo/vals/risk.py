import yfinance as yf
import numpy as np

def calculate_risk_score(ticker):
    al_score = get_AL_ratio_score(ticker)
    pe_score = get_PE_ratio_score(ticker)
    vol_score = get_volatility_score(ticker)
    strength_score = get_overall_strength_score(ticker)

    # Weighted total score
    total_score = (
        0.3 * al_score +
        0.2 * pe_score +
        0.3 * vol_score +
        0.2 * strength_score
    )

    # Convert score to risk: higher total score -> lower risk
    risk_score = 100 - total_score  # Inverting the score to represent risk from 1 (low) to 100 (high)

    return round(risk_score, 2)

def get_AL_ratio_score(ticker):
    ticker = yf.Ticker(ticker)
    try:
        balance_sheet = ticker.balance_sheet
        total_assets = balance_sheet.loc["Total Assets"].iloc[0]  # Use .iloc for positional indexing
        total_liabilities = balance_sheet.loc["Total Liabilities Net Minority Interest"].iloc[0]  # Use .iloc for positional indexing
        al_ratio = total_assets / total_liabilities if total_liabilities else 0
        
        # Score AL ratio: higher ratio is lower risk
        score = min(100, max(0, (al_ratio - 1) * 20))
        return score
    except Exception as e:
        print(f"Error calculating AL ratio score: {e}")
        return 50  # Average score if data is unavailable

def get_PE_ratio_score(ticker):
    ticker = yf.Ticker(ticker)
    try:
        pe_ratio = ticker.info.get("trailingPE")
        # Normalize P/E: moderate values score higher
        score = 100 - min(100, abs(pe_ratio - 15) * 5) if pe_ratio else 50
        return score
    except Exception as e:
        print(f"Error calculating PE ratio score: {e}")
        return 50

def get_volatility_score(ticker):
    ticker = yf.Ticker(ticker)
    try:
        hist = ticker.history(period="3mo")
        daily_returns = hist['Close'].pct_change().dropna()
        volatility = np.std(daily_returns)
        # Higher volatility -> Higher risk, so invert the score
        score = max(0, min(100, (0.05 - volatility) * 2000))  # Tweak as needed
        return score
    except Exception as e:
        print(f"Error calculating volatility score: {e}")
        return 50

def get_overall_strength_score(ticker):
    ticker = yf.Ticker(ticker)
    try:
        revenue_growth = ticker.info.get("revenueGrowth")
        score = min(100, max(0, revenue_growth * 100)) if revenue_growth else 50
        return score
    except Exception as e:
        print(f"Error calculating overall strength score: {e}")
        return 50

