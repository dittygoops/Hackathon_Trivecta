from openai import OpenAI
import os
from dotenv import load_dotenv
from algo import fin_val


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
            "content": "Top 20 companies related to oil within the US stock market and are being actively traded"
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
    # Get response from LLM
    llm_output = get_llm_response("oil")
    print(llm_output)

    # # Extract tickers
    # tickers = extract_tickers(llm_output)
    # print(tickers)
    
    # # Example of looping over tickers
    # for ticker in tickers:
    #     print(f"Processing ticker: {ticker}")
    #     # Add your ticker processing logic here
    #     values_instance = fin_val.Values(ticker)  # Replace with actual values if needed
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