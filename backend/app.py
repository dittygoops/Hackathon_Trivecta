# import the Flask class from the flask module
from flask import Flask, request, jsonify
import llm_search.stock_search as stock_search
import json

# create the application object
app = Flask(__name__)

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

def main():
    app.run(port=5000)

if __name__ == "__main__":
    main()