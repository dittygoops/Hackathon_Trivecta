from vals import dcf
import yfinance as yf
from vals import risk

class Values:
    def __init__(self, ticker):
        self.ticker = ticker

    def getValuation(self, ticker):
        try:
            ImpliedVal = dcf.DCF_Implied_Value(ticker, forecast_years=5, discount_rate=0.02, perpetual_growth_rate=0.01)
        except Exception as e:
            print(f"Error in DCF calculation: {e}")
            ImpliedVal = 0

        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")
        current_price = hist['Close'].iloc[-1]
        
        perGrowth = 2
         
        if ImpliedVal != 0:
             perGrowth = ((ImpliedVal - current_price*3)/current_price)/10
             perGrowth = perGrowth/1.65


        if perGrowth < 10 and perGrowth > 0:
            perGrowth = perGrowth * 85


        return perGrowth
    
    def getRiskScore(self, ticker):
        risk_score = risk.calculate_risk_score(ticker)
        return risk_score
    
    def valuation_vals(self, ticker):
        
        RevenueGrowth = self.getValuation(ticker)
        RiskVal = self.getRiskScore(ticker)

        return RevenueGrowth, RiskVal
