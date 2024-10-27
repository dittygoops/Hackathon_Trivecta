# import fin_val
import fin_val
import alpaca_connect.alpaca as ap

ticker = "NVDA"

if __name__ == "__main__":
    # Create an instance of the Values class
    values_instance = fin_val.Values(ticker)
    # values_instance = Values(ticker)  # Replace with actual values if needed
    # Call the getValuation method
    valuation = round(values_instance.getValuation(ticker=ticker),2)
    print(valuation)
    risk_val = values_instance.getRiskScore(ticker=ticker)
    print(risk_val)


