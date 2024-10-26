import vals.dcf as dcf
import yfinance as yf

class Values:
    def __init__(self, DCF, PEG, PE, AL_ratio):
        self.DCF = DCF
        self.PEG = PEG
        self.PE = PE
        self.AL_ratio = AL_ratio

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
        # Placeholder logic for risk score
        return 1  # replace with actual risk score calculation logic
    
    def valuation_vals(self, ticker):
        RevenueGrowth = self.getValuation(ticker)
        #RiskVal = self.getRiskScore(ticker)
        #return RevenueGrowth, RiskVal
        return RevenueGrowth
