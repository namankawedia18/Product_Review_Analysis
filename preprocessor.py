# ============================================================
# preprocessor.py
# Classical AI - Text Preprocessing (Symbolic NLP)
# No ML — just rule-based text cleaning
# ============================================================

import string
from knowledge_base import STOPWORDS


def preprocess(text):
    """
    Cleans and tokenizes a review text.
    Steps:
      1. Lowercase
      2. Remove punctuation
      3. Tokenize (split into words)
      4. Remove stopwords
    Returns: list of clean tokens
    """

    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Step 3: Tokenize
    tokens = text.split()

    # Step 4: Remove stopwords
    tokens = [word for word in tokens if word not in STOPWORDS]

    return tokens


# Quick test
if __name__ == "__main__":
    sample = "This phone is excellent! Battery life is amazing, but the camera is poor."
    result = preprocess(sample)
    print("Tokens:", result)
