# simple template for app.py
# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"

def main():
    app.run()

if __name__ == "__main__":
    main()