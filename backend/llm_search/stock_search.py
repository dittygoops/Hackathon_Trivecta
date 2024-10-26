from openai import OpenAI
import os
from dotenv import load_dotenv

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
            "content": "Top 20 companies related to {input}"
        }
    ]
    
    response = client.chat.completions.create(
        model="llama-3.1-sonar-large-128k-online",
        messages=messages,
        stream=False
    )
    
    return response.choices[0].message.content

def extract_tickers(text):
    """Extract just the ticker symbols from the text"""
    tickers = []
    lines = text.split('\n')
    
    for line in lines:
        if '**' in line:
            start = line.find('**') + 2
            end = line.find('**', start)
            if start != -1 and end != -1:
                ticker = line[start:end].strip()
                tickers.append(ticker)
    
    return tickers

def main():
    # Get response from LLM
    llm_output = get_llm_response("technology")

    # Extract tickers
    tickers = extract_tickers(llm_output)
    
    # Example of looping over tickers
    for ticker in tickers:
        print(f"Processing ticker: {ticker}")
        # Add your ticker processing logic here
        
if __name__ == "__main__":
    main()