# # import the Flask class from the flask module
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import llm_search.stock_search as stock_search
# import json, os, logging
# from alpaca_connect import alpaca
# from dotenv import load_dotenv
# from openai import OpenAI
# from functools import lru_cache

# # create the application object
# app = Flask(__name__)
# CORS(app)

# # use decorators to link the function to a url
# @app.route('/')
# def home():
#     return "Hello, World!"

# logger = logging.getLogger(__name__)

# class LLM:
#     def __init__(self):
#         self._load_environment()
#         self.client = self._initialize_client()
    
#     def _load_environment(self) -> None:
#         """Load environment variables safely."""
#         if not load_dotenv():
#             logger.warning("No .env file found")
        
#         self.api_key = os.getenv('PERPLEXITY_API_KEY')
#         if not self.api_key:
#             raise ValueError("PERPLEXITY_API_KEY not found in environment variables")
    
#     def _initialize_client(self) -> OpenAI:
#         """Initialize OpenAI client with error handling."""
#         try:
#             return OpenAI(
#                 api_key=self.api_key,
#                 base_url="https://api.perplexity.ai"
#             )
#         except Exception as e:
#             logger.error(f"Failed to initialize OpenAI client: {e}")
#             raise

#     @lru_cache(maxsize=100)
#     def get_llm_response(self, query: str) -> str:
#         """Cache and get stock recommendations from LLM."""
#         try:
#             messages = [
#                 {"role": "system", "content": "You are a stock market assistant that gives short concise answers to the user's questions. Don't add extra formatting or information. Just answer the user's question. Make the response less than 200 characters."},
#                 {
#                     "role": "user",
#                     "content": str(query)
#                 }
#             ]
            
#             response = self.client.chat.completions.create(
#                 model="llama-3.1-sonar-large-128k-online",
#                 messages=messages,
#                 stream=False
#             )
            
#             return response.choices[0].message.content
#         except Exception as e:
#             logger.error(f"Error getting LLM response: {e}")
#             raise

# @app.route('/search', methods=['POST'])
# def search():
#     data = request.get_json()
#     query_input = data.get('query')
    
#     if not query_input:
#         return jsonify({"error": "Query parameter is missing"}), 400
    
#     try:
#         result = stock_search.query(query_input)
#         return jsonify(json.loads(result))
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# @app.route('/submit_query', methods=['POST'])
# def submit_query():
#     data = request.get_json()
    
#     # Extract all required data from request
#     tickers = data.get('tickers')
#     api_key = data.get('API_key')
#     api_secret = data.get('API_secret')
#     money = data.get('money')
    
#     # Validate all required inputs
#     if not all([tickers, api_key, api_secret, money]):
#         return jsonify({
#             "error": "Missing required parameters: tickers, API_key, API_secret, and money must be provided"
#         }), 400
    
#     if not isinstance(tickers, list):
#         return jsonify({
#             "error": "Tickers must be provided as a list"
#         }), 400
        
#     if not isinstance(money, (int, float)) or money <= 0:
#         return jsonify({
#             "error": "Money must be a positive number"
#         }), 400
#     return alpaca.port_buy(api_key, api_secret, tickers, money)

# @app.route('/query-llm', methods=['POST'])
# def query_llm():
#     # Get the JSON data from the request
#     data = request.get_json()
#     query = data.get('query')
#     print('got json')
    
#     # Validate the query parameter
#     if not query:
#         return jsonify({
#             "error": "Query parameter is missing"
#         }), 400
        
#     try:
#         # Get response from LLM
#         llm_response = LLM().get_llm_response(query)
        
#         return jsonify({
#             "status": "success",
#             "response": llm_response
#         })
        
#     except Exception as e:
#         return jsonify({
#             "error": f"Failed to process LLM query: {str(e)}"
#         }), 500

# def main():
#     app.run(port=5000)

# if __name__ == "__main__":
#     main()

DJ Tiger
.djtiger
Invisible

DJ Tiger — 10/20/2024 5:22 PM
bro i lost 10 out of 77 points cuz i didn't read the NOT
dittygoops — 10/20/2024 5:22 PM
oh shit
DJ Tiger — 10/20/2024 5:22 PM
like im going to kill myself
no
i got a 59
dittygoops — 10/20/2024 5:22 PM
bruh
DJ Tiger — 10/20/2024 5:22 PM
but it doesn't matter
dittygoops — 10/20/2024 5:22 PM
there will be a curve hopefully
also
DJ Tiger — 10/20/2024 5:22 PM
cu the midterm is only 10 percent of the overall grade
yeah
dittygoops — 10/20/2024 5:22 PM
the test doesnt matter
yeah
DJ Tiger — 10/20/2024 5:23 PM
yeah thankfully
but i gotta lock in
especilaly for the project
and also 230
dittygoops — 10/20/2024 5:23 PM
ya
DJ Tiger — 10/20/2024 5:45 PM
wiat
bro
im dumb
shiva i think got a 92
i might need to sotp coding now
dittygoops — 10/20/2024 5:45 PM
yeah i saw that 💀
DJ Tiger — 10/20/2024 5:45 PM
bro
im an actual idiot
LMFAOAOAO
dittygoops — 10/20/2024 5:45 PM
nah ur not
DJ Tiger — 10/20/2024 5:45 PM
💀
dittygoops — 10/20/2024 5:45 PM
this shits useless anyways
like
think about it
ur already pressed on time
DJ Tiger — 10/20/2024 5:45 PM
yeah, but like SHIVA
brother
dittygoops — 10/20/2024 5:45 PM
and he's just getting like 1.5 % more than u
DJ Tiger — 10/20/2024 5:46 PM
oh yeah
that's honestly true
dittygoops — 10/20/2024 5:46 PM
imagine how much time he spent for just 1.5%
did quizlets and stuff
ur ifne
fine
DJ Tiger — 10/20/2024 5:46 PM
this tbh
thank you ditty goops
you're my goat man
DJ Tiger — Yesterday at 11:32 AM
https://docs.google.com/forms/d/e/1FAIpQLSeCKJav-z97H3KkEw5fha2gTGCv_Eq7Y79W_OzD9zeQAY0QuQ/viewform
Google Docs
Pick your preferred Track!
Only one person from each team should fill out this form.
Image
DJ Tiger — Yesterday at 9:49 PM
PERPLEXITY_API_KEY="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"
DJ Tiger — Yesterday at 10:16 PM
# from typing import List, Dict, Optional
# from openai import OpenAI
# import os
# from dotenv import load_dotenv
# from algo import fin_val
# import re
Expand
message.txt
12 KB
from typing import List, Dict, Optional
from openai import OpenAI
import os
from dotenv import load_dotenv
from algo import fin_val
import re
Expand
message.txt
6 KB
DJ Tiger — Today at 12:27 AM
from typing import List, Dict, Optional
from openai import OpenAI
import os
from dotenv import load_dotenv
from algo import fin_val
import re
Expand
message.txt
6 KB
DJ Tiger — Today at 8:47 AM
alpaca.py
import yfinance as yf
import requests
import json

class StockOrder:
    def __init__(self, ticker, price, quantity):
Expand
message.txt
3 KB
import yfinance as yf
import requests
import json

class StockOrder:
    def __init__(self, ticker, price, quantity):
Expand
message.txt
3 KB
dittygoops — Today at 9:38 AM
# import the Flask class from the flask module
from flask import Flask, request, jsonify
from flask_cors import CORS
import llm_search.stock_search as stock_search
import json, os, logging
from alpaca_connect import alpaca
from dotenv import load_dotenv
from openai import OpenAI
from functools import lru_cache

# create the application object
app = Flask(__name__)
CORS(app)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"

logger = logging.getLogger(__name__)

class LLM:
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
    def get_llm_response(self, query: str) -> str:
        """Cache and get stock recommendations from LLM."""
        try:
            messages = [
                {"role": "system", "content": "You are a stock market assistant that gives short concise answers to the user's questions. Don't add extra formatting or information. Just answer the user's question. Make the response less than 200 characters."},
                {
                    "role": "user",
                    "content": str(query)
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

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query_input = data.get('query')
    
    if not query_input:
        return jsonify({"error": "Query parameter is missing"}), 400
    
    try:
        result = stock_search.query(query_input)
        return jsonify(json.loads(result))
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/submit_query', methods=['POST'])
def submit_query():
    data = request.get_json()
    
    # Extract all required data from request
    tickers = data.get('tickers')
    api_key = data.get('API_key')
    api_secret = data.get('API_secret')
    money = data.get('money')
    
    # Validate all required inputs
    if not all([tickers, api_key, api_secret, money]):
        return jsonify({
            "error": "Missing required parameters: tickers, API_key, API_secret, and money must be provided"
        }), 400
    
    if not isinstance(tickers, list):
... (41 lines left)
Collapse
message.txt
5 KB
﻿
dittygoops
dittygoops
 
 
 
chess.com/member/dittygoops
# import the Flask class from the flask module
from flask import Flask, request, jsonify
from flask_cors import CORS
import llm_search.stock_search as stock_search
import json, os, logging
from alpaca_connect import alpaca
from dotenv import load_dotenv
from openai import OpenAI
from functools import lru_cache

# create the application object
app = Flask(__name__)
CORS(app)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"

logger = logging.getLogger(__name__)

class LLM:
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
    def get_llm_response(self, query: str) -> str:
        """Cache and get stock recommendations from LLM."""
        try:
            messages = [
                {"role": "system", "content": "You are a stock market assistant that gives short concise answers to the user's questions. Don't add extra formatting or information. Just answer the user's question. Make the response less than 200 characters."},
                {
                    "role": "user",
                    "content": str(query)
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

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query_input = data.get('query')
    
    if not query_input:
        return jsonify({"error": "Query parameter is missing"}), 400
    
    try:
        result = stock_search.query(query_input)
        return jsonify(json.loads(result))
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/submit_query', methods=['POST'])
def submit_query():
    data = request.get_json()
    
    # Extract all required data from request
    tickers = data.get('tickers')
    api_key = data.get('API_key')
    api_secret = data.get('API_secret')
    money = data.get('money')
    
    # Validate all required inputs
    if not all([tickers, api_key, api_secret, money]):
        return jsonify({
            "error": "Missing required parameters: tickers, API_key, API_secret, and money must be provided"
        }), 400
    
    if not isinstance(tickers, list):
        return jsonify({
            "error": "Tickers must be provided as a list"
        }), 400
        
    if not isinstance(money, (int, float)) or money <= 0:
        return jsonify({
            "error": "Money must be a positive number"
        }), 400
    return alpaca.port_buy(api_key, api_secret, tickers, money)

@app.route('/query-llm', methods=['POST'])
def query_llm():
    # Get the JSON data from the request
    data = request.get_json()
    query = data.get('query')
    
    # Validate the query parameter
    if not query:
        return jsonify({
            "error": "Query parameter is missing"
        }), 400
        
    try:
        # Get response from LLM
        llm_response = LLM().get_llm_response(query)
        
        return jsonify({
            "status": "success",
            "response": llm_response
        })
        
    except Exception as e:
        return jsonify({
            "error": f"Failed to process LLM query: {str(e)}"
        }), 500

def main():
    app.run(port=5000)

if __name__ == "__main__":
    main()
