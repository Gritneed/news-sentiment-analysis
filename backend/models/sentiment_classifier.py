import os
import pickle
from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Paths
MODEL_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(MODEL_DIR, 'sentiment_model.pkl')

# Sample training data
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
    ("Debt levels have increased significantly", "negative"),
]


def train_simple_model() -> Pipeline:
    """
    Train a simple sentiment classification model.

    Returns:
        Pipeline: A trained Scikit-learn pipeline.
    """
    texts = [text for text, label in SAMPLE_DATA]
    labels = [label for text, label in SAMPLE_DATA]

    pipeline = Pipeline([
        ('vectorizer', TfidfVectorizer(max_features=5000)),
        ('classifier', MultinomialNB())
    ])

    pipeline.fit(texts, labels)

    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(pipeline, f)

    return pipeline


def load_or_train_model() -> Pipeline:
    """
    Load model from file or train it if not found.

    Returns:
        Pipeline: The trained or loaded model.
    """
    if os.path.exists(MODEL_PATH):
        try:
            with open(MODEL_PATH, 'rb') as f:
                return pickle.load(f)
        except Exception:
            print("⚠️ Failed to load model. Training a new one.")
            return train_simple_model()
    else:
        return train_simple_model()


# Load model on module import
sentiment_model = load_or_train_model()


def classify_sentiment(text: str) -> str:
    """
    Predict sentiment label from input text.

    Args:
        text (str): Preprocessed input string.

    Returns:
        str: Sentiment label ('positive', 'neutral', or 'negative').
    """
    if not text or text.strip() == "":
        return "neutral"

    return sentiment_model.predict([text])[0]


if __name__ == "__main__":
    test_phrases: List[str] = [
        "The company reported strong earnings growth",
        "Revenue declined sharply after poor results",
        "The company announced layoffs amid declining sales",
        "",
        "Analysts remain cautious on Tesla's stock performance."
    ]

    for phrase in test_phrases:
        sentiment = classify_sentiment(phrase)
        print(f"'{phrase}' -> Sentiment: {sentiment}")
