from typing import List, Dict, Optional
from openai import OpenAI
import os
from dotenv import load_dotenv
from algo import fin_val
import re
import json
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
import logging
from dataclasses import dataclass
from pathlib import Path
import argparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class StockData:
    """Data class for storing stock information."""
    ticker: str
    description: str
    growth_potential: float = 0.0
    risk_score: float = 0.0

class StockDataProcessor:
    """Class to handle stock data processing operations."""
    
    def __init__(self):
        self._load_environment()
        self.client = self._initialize_client()
        
    def _load_environment(self) -> None:
        """Load environment variables safely."""
        if not load_dotenv():
            logger.warning("No .env file found")
        
        self.api_key = os.getenv('PERPLEXITY_API_KEY')
        if not self.api_key:
            raise ValueError("PERPLEXITY_API_KEY not found in environment variables")

    def _initialize_client(self) -> OpenAI:
        """Initialize OpenAI client with error handling."""
        try:
            return OpenAI(
                api_key=self.api_key,
                base_url="https://api.perplexity.ai"
            )
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            raise

    @lru_cache(maxsize=100)
    def get_llm_response(self, topic: str) -> str:
        """Cache and get stock recommendations from LLM."""
        try:
            messages = [
                {"role": "system", "content": "You are a helpful stock market assistant."},
                {
                    "role": "user",
                    "content": (
                        f"Please provide a list of the top 20 {topic} related "
                        "stocks currently being actively traded in the US market. "
                        "Format each entry as follows: [ticker] - description. "
                        "Only return the ticker and description without any extra "
                        "text or explanation."
                    )
                }
            ]
            
            response = self.client.chat.completions.create(
                model="llama-3.1-sonar-large-128k-online",
                messages=messages,
                stream=False
            )
            
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error getting LLM response: {e}")
            raise

    def parse_stock_list(self, text: str) -> List[StockData]:
        """Parse the stock list using improved regex pattern."""
        pattern = r"\*\*([A-Z]+)\*\*\s+-\s+(.+)"
        try:
            matches = re.findall(pattern, text)
            return [StockData(ticker=match[0], description=match[1]) for match in matches]
        except Exception as e:
            logger.error(f"Error parsing stock list: {e}")
            raise

    def process_single_stock(self, stock: StockData) -> Optional[Dict]:
        """Process a single stock with error handling."""
        try:
            values_instance = fin_val.Values(stock.ticker)
            
            return {
                "ticker": stock.ticker,
                "description": stock.description,
                "growth_potential": round(values_instance.getValuation(ticker=stock.ticker), 2),
                "risk_score": values_instance.getRiskScore(ticker=stock.ticker)
            }
        except Exception as e:
            logger.error(f"Error processing stock {stock.ticker}: {e}")
            return None

    def query_stock_data(self, topic: str, max_workers: int = 4) -> str:
        """Process stock data concurrently and return formatted JSON."""
        try:
            llm_output = self.get_llm_response(topic)
            stock_data = self.parse_stock_list(llm_output)
            
            # Process stocks concurrently
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                results = list(executor.map(self.process_single_stock, stock_data))
            
            # Filter out None values from failed processing
            valid_results = [r for r in results if r is not None]

            return json.dumps(valid_results, indent=4)
            
        except Exception as e:
            logger.error(f"Error in query_stock_data: {e}")
            raise

def get_topic_input() -> str:
    """Get topic input from user if not provided as command line argument."""
    return input("Enter the market sector/topic (e.g., technology, healthcare, energy): ").strip()

def query(query):
    """Main function with error handling and topic input."""
    try:
        processor = StockDataProcessor()
        result = processor.query_stock_data(query)
        return result
        
    except Exception as e:
        logger.error(f"Main function error: {e}")
        raise