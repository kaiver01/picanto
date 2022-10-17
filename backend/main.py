# flask server

from datetime import datetime
from flask import Flask, render_template, request
 
app = Flask(__name__) 
 
@app.route("/") 
def index(): 
    return render_template('index.html')

@app.route("/oven_start", methods=['POST'])
def oven_start():
    print(request.json)
    return "ok"

@app.route("/tracker", methods=['GET'])
def tracker(): 
    return render_template('tracker.html')

@app.route("/cashier", methods=['GET']) 
def cashier(): 
    return render_template('cashier.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)