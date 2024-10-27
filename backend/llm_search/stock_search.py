from openai import OpenAI
import os
from dotenv import load_dotenv
from typing import List, Dict, Tuple
import sys
from pathlib import Path

# Get the absolute path to the backend directory
current_dir = Path(__file__).resolve().parent
backend_dir = current_dir.parent
sys.path.append(str(backend_dir))

# Now import the algo module
import algo.fin_val as fin_val

# Rest of your code remains the same...
def get_llm_response(input_sector: str) -> str:
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
            "content": f"Top 50 companies related to {input_sector}. Format each line as: **TICKER** - Description"
        }
    ]
    
    response = client.chat.completions.create(
        model="llama-3.1-sonar-large-128k-online",
        messages=messages,
        stream=False
    )
    
    return response.choices[0].message.content

def extract_stock_info(text: str) -> List[Dict[str, str]]:
    stocks = []
    lines = text.split('\n')
    
    for line in lines:
        if not line.strip() or '**' not in line:
            continue
            
        try:
            ticker_start = line.find('**') + 2
            ticker_end = line.find('**', ticker_start)
            ticker = line[ticker_start:ticker_end].strip()

            desc_parts = line.split('-', 1)
            if len(desc_parts) > 1:
                description = desc_parts[1].strip()
            else:
                description = ""
                
            stocks.append({
                "ticker": ticker,
                "description": description
            })
            
        except Exception as e:
            print(f"Error processing line: {line}")
            print(f"Error: {str(e)}")
            continue
    
    return stocks

def main():
    sector = "technology"
    llm_output = get_llm_response(sector)
    stocks = extract_stock_info(llm_output)
        
    for stock in stocks:
        ticker = stock['ticker']
        val = fin_val.valuation_vals(ticker)
        
if __name__ == "__main__":
    main()