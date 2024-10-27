from typing import Dict, List
from openai import OpenAI
import os
from dotenv import load_dotenv
from .algo import fin_val
import re
import json

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
            "content": "Please provide a list of the top 20 technology related stocks currently being actively traded in the US market. Format each entry as follows: [ticker] - description. Only return the ticker and description without any extra text or explanation."
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
def query(query_from_user):
    # Get response from LLM
    llm_output = get_llm_response(query_from_user)
    stock_json_array = []

    # Extract tickers
    stock_data = parse_stock_list(llm_output)
    tickers = [stock['ticker'] for stock in stock_data]

    # Extract description values
    descriptions = [stock['description'] for stock in stock_data]

    for ticker, description in zip(tickers, descriptions):
        print(f"Processing {ticker}: {description}")
    
        # Initialize the financial values instance
        values_instance = fin_val.Values(ticker)
        
        # Get the valuation, round it to two decimal places
        valuation = round(values_instance.getValuation(ticker=ticker), 2)
        
        # Get the risk score
        risk_val = values_instance.getRiskScore(ticker=ticker)
        
        # Create a JSON object with ticker, description, valuation, and risk score
        stock_json_object = {
            "ticker": ticker,
            "description": description,
            "growth_potential": valuation,
            "risk_score": risk_val
        }
    
        # Append the JSON object to the array
        stock_json_array.append(stock_json_object)

    # Convert the list of JSON objects into a JSON array (string)
    stock_json_array_str = json.dumps(stock_json_array, indent=4)

    # Print or return the JSON array
    return stock_json_array_str