import re
from typing import List

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Optional: run these once
# nltk.download('punkt')
# nltk.download('stopwords')


def preprocess_text(text: str) -> str:
    """
    Lowercase, remove punctuation, tokenize, and remove English stopwords.

    Args:
        text (str): Raw input string.

    Returns:
        str: Preprocessed text.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]
    return " ".join(tokens)


if __name__ == "__main__":
    sample_text = "Tesla stock plunged 15 percent on Monday, its steepest drop in five years."
    processed_result = preprocess_text(sample_text)
    print(f"Original: {sample_text}")
    print(f"Processed: {processed_result}")