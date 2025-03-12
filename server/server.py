from flask import Flask, jsonify
from flask_cors import CORS
from .stocktool import get_market_data

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/market-data', methods=['GET'])
    def market_data():
        return jsonify(get_market_data())
    
    return app

def main():
    app = create_app()
    app.run(port=5001, debug=True)

if __name__ == '__main__':
    main()