from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests
import logging
import os

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/fear-greed-index')
def get_fear_greed_index():
    try:
        url = 'https://api.alternative.me/fng/'
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        fear_greed_value = int(data['data'][0]['value'])
        fear_greed_sentiment = data['data'][0]['value_classification']
        return jsonify({'value': fear_greed_value, 'sentiment': fear_greed_sentiment})
    except Exception as e:
        app.logger.error(f"Error in /fear-greed-index: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/stock-news')
def get_stock_news():
    try:
        api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
        if not api_key:
            return jsonify({'error': 'Alpha Vantage API key not found. Please set the ALPHA_VANTAGE_API_KEY environment variable.'}), 500
        url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&apikey={api_key}'
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        articles = []
        counter = 0
        for item in data['feed']:
            # if counter < 36:
            #     counter += 1
            #     continue
            if item['source'] == "The Motley Fool":
                continue
            sentiment = "Neutral"
            if item['ticker_sentiment']:
                top_ticker = max(item['ticker_sentiment'], key=lambda x: x.get('relevance_score', 0) or 0)
                if top_ticker:
                    sentiment = top_ticker['ticker_sentiment_label']

            articles.append({
                'title': item['title'],
                'link': item['url'],
                'sentiment': sentiment,
                'source': item['source']
            })
        return jsonify(articles)
    except Exception as e:
        app.logger.error(f"Error in /stock-news: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)