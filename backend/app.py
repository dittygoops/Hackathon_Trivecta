# import the Flask class from the flask module
from flask import Flask, request, jsonify
from flask_cors import CORS
import llm_search.stock_search as stock_search
import json
from .alpaca_connect import alpaca

# create the application object
app = Flask(__name__)
CORS(app)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"

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
    alpaca.port_buy(api_key, api_secret, tickers, money)

def main():
    app.run(port=5000)

if __name__ == "__main__":
    main()