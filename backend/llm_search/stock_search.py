from typing import Dict, List
from openai import OpenAI
import os
from dotenv import load_dotenv
from algo import fin_val
import re

def get_llm_response(input):
    """Get stock recommendations from LLM"""
    load_dotenv()
    api_key = os.getenv('PERPLEXITY_API_KEY')
    
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.perplexity.ai"
    )
    
    messages = [
        {
            "role": "system",
            "content": "You are a helpful stock market assistant"
        },
        {
            "role": "user",
            "content": "Please provide a list of the top 20 technology stocks currently being actively traded in the US market. Format each entry as follows: [ticker] - description. Only return the ticker and description without any extra text or explanation."
        }
    ]
    
    response = client.chat.completions.create(
        model="llama-3.1-sonar-large-128k-online",
        messages=messages,
        stream=False
    )
    
    return response.choices[0].message.content

def parse_stock_list(text):
    # Regular expression to match the stock entries in the format [ticker] - description
    pattern = r"\*\*([A-Z]+)\*\*\s+-\s+(.+)"
    matches = re.findall(pattern, text)

    # Creating a list of dictionaries to store ticker and description pairs
    stocks = [{"ticker": match[0], "description": match[1]} for match in matches]

    return stocks
def main():
    # Get response from LLM
    llm_output = get_llm_response("oil")
    # print(llm_output)

    # Extract tickers
    tickers = parse_stock_list(llm_output)
    # print(tickers)
    
    # Example of looping over tickers
    # for ticker in tickers:
    #     print(f"Processing ticker: {ticker}")
    #     # Add your ticker processing logic here
    #     values_instance = fin_val.Values(ticker[ticker['ticker']])  # Replace with actual values if needed
    #     # Call the getValuation method
    #     try:
    #         valuation = round(values_instance.getValuation(ticker=ticker),2)
    #         print(valuation)
    #         risk_val = values_instance.getRiskScore(ticker=ticker)
    #         print(risk_val)
    #     except Exception as e:
    #         print(f"Error processing ticker {ticker}: {e}")
    

        
if __name__ == "__main__":
    main()