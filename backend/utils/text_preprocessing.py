import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Only run the downloads the first time:
# nltk.download('punkt')
# nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenize text
    stop_words = set(stopwords.words('english'))  # Get stopwords
    tokens = [token for token in tokens if token not in stop_words]  # Remove stopwords
    
    return ' '.join(tokens)  # Convert list back to a string ✅ FIX

if __name__ == "__main__":
    sample_text = "Tesla stock plunged 15 percent on Monday, its steepest drop in five years."
    processed_result = preprocess_text(sample_text)
    print(processed_result)
