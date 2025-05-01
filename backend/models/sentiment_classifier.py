import os
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Path to save/load the model
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(MODEL_DIR, 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl')

# Example financial phrases with sentiment labels (we'll use these for initial training)
# Later, this would be replaced with proper Financial PhraseBank data
SAMPLE_DATA = [
    ("The company reported strong earnings growth", "positive"),
    ("Quarterly revenue exceeded analyst expectations", "positive"),
    ("Shares surge on positive earnings report", "positive"),
    ("Company announces expansion plans", "positive"),
    ("Profit margins improved significantly", "positive"),
    
    ("The company reported mixed results", "neutral"),
    ("Earnings were in line with expectations", "neutral"),
    ("The market had a muted response to the announcement", "neutral"),
    ("The stock price remained stable after the news", "neutral"),
    ("Analysts maintain a hold rating on the stock", "neutral"),
    
    ("The company missed earnings targets", "negative"),
    ("Revenue declined year-over-year", "negative"),
    ("The company announced layoffs", "negative"),
    ("Shares plummeted on disappointing guidance", "negative"),
    ("Debt levels have increased significantly", "negative")
]

def train_simple_model():
    """Train a simple sentiment model and save it"""
    # Extract text and labels
    texts = [item[0] for item in SAMPLE_DATA]
    labels = [item[1] for item in SAMPLE_DATA]
    
    # Create TF-IDF vectorizer and Naive Bayes classifier in a pipeline
    pipeline = Pipeline([
        ('vectorizer', TfidfVectorizer(max_features=5000)),
        ('classifier', MultinomialNB())
    ])
    
    # Train the model
    pipeline.fit(texts, labels)
    
    # Save the model
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(pipeline, f)
    
    return pipeline

def load_or_train_model():
    """Load existing model or train a new one if none exists"""
    if os.path.exists(MODEL_PATH):
        try:
            with open(MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
            return model
        except:
            print("Error loading model, training a new one.")
            return train_simple_model()
    else:
        return train_simple_model()

# Load or train model on module import
sentiment_model = load_or_train_model()

def classify_sentiment(text):
    """
    Classify sentiment of a given text
    
    Args:
        text (str): Preprocessed text
        
    Returns:
        str: Sentiment label (positive, neutral, negative)
    """
    if not text or text.strip() == "":
        return "neutral"  # Default for empty text
    
    # Make prediction
    prediction = sentiment_model.predict([text])[0]
    return prediction

if __name__ == "__main__":
    # Example test phrases
    test_phrases = [
        "The company reported strong earnings growth",
        "Revenue declined sharply after poor results",
        "The company announced layoffs amid declining sales",
        "",
        "Analysts remain cautious on Tesla's stock performance."
    ]

    # Explicitly test classification on sample phrases
    for phrase in test_phrases:
        sentiment = classify_sentiment(phrase)
        print(f"'{phrase}' -> Sentiment: {sentiment}")