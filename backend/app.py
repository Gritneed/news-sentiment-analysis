from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
import json
import logging
from dotenv import load_dotenv  # For loading environment variables

# Load .env file (API key)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Add backend folder to system path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR, "api"))
sys.path.append(os.path.join(BASE_DIR, "utils"))
sys.path.append(os.path.join(BASE_DIR, "models"))

from api.news_fetcher import fetch_news_articles
from utils.text_preprocessing import preprocess_text
from models.sentiment_classifier import classify_sentiment

# Logging Configuration
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
#CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
# CORS(app)
#CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)


@app.after_request
def add_cors_headers(response):
    """プリフライトリクエストの CORS ヘッダーを明示的に追加"""
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

# Configuration
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
print(f"DEBUG: NEWS_API_KEY={NEWS_API_KEY}")

if not NEWS_API_KEY:
    logger.warning("⚠️ NEWS_API_KEY is not set. API calls may fail.")

@app.route('/api/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'News Sentiment Analyzer API is running'})

@app.route('/api/analyze', methods=['POST'])
def analyze_company():
    """Analyze sentiment for a given company"""
    data = request.json
    print("Received request data:", data)
    if not data or 'company' not in data:
        return jsonify({'error': 'Missing company name'}), 400
    
    company_name = data['company']
    days_back = data.get('days_back', 7)  # Default to last 7 days
    
    try:
        # Fetch news articles
        articles = fetch_news_articles(company_name, NEWS_API_KEY, days_back)
        
        if not articles or 'articles' not in articles or len(articles['articles']) == 0:
            return jsonify({'message': f'No recent news found for {company_name}'}), 404
        
        # Process each article
        processed_results = []
        sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
        
        for article in articles['articles']:
            content = article.get('content', article.get('description', ''))

            logger.debug(f"Raw content: {content}")  
            logger.debug(f"Type of content: {type(content)}")  
            
            if not content:
                continue
                
            # Preprocess the text
            preprocessed_text = preprocess_text(content)
            
            # Classify sentiment
            sentiment = classify_sentiment(preprocessed_text)
            
            # Increment sentiment counter
            sentiments[sentiment] += 1
            
            # Add to results
            processed_results.append({
                'title': article.get('title', 'No title'),
                'url': article.get('url', ''),
                'sentiment': sentiment,
                'published_at': article.get('publishedAt', '')
            })
        
        # Calculate overall sentiment
        total_articles = len(processed_results)
        sentiment_percentages = {
            k: round(v * 100 / total_articles, 2) if total_articles > 0 else 0 
            for k, v in sentiments.items()
        }
        
        dominant_sentiment = max(sentiments, key=sentiments.get)
        
        return jsonify({
            'company': company_name,
            'article_count': total_articles,
            'sentiment_counts': sentiments,
            'sentiment_percentages': sentiment_percentages,
            'dominant_sentiment': dominant_sentiment,
            'articles': processed_results
        })
        
    except Exception as e:
        logger.exception("Exception occurred in /api/analyze")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)