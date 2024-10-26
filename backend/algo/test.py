import backend.algo.fin_val as fin_val

ticker = "BABA"

if __name__ == "__main__":
    # Create an instance of the Values class
    values_instance = fin_val.Values(DCF=0, PEG=0, PE=0, AL_ratio=0)  # Replace with actual values if needed
    # Call the getValuation method
    valuation = round(values_instance.getValuation(ticker=ticker),2)
    print(valuation)
