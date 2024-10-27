import fin_val

ticker = "NVDA"

if __name__ == "__main__":
    # Create an instance of the Values class
    values_instance = fin_val.Values(ticker)  # Replace with actual values if needed
    # Call the getValuation method
    valuation = round(values_instance.getValuation(ticker=ticker),2)
    print('Rev Val: ' + str(valuation))
    risk_val = values_instance.getRiskScore(ticker=ticker)
    print('Risk Score: ' + str(risk_val))