from flask import Flask, jsonify
from flask_cors import CORS
from stocktool import get_market_data

app = Flask(__name__)
CORS(app)

@app.route('/market-data', methods=['GET'])
def market_data():
    return jsonify(get_market_data())

if __name__ == '__main__':
    app.run(port=5001, debug=True)