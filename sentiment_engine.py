# ============================================================
# sentiment_engine.py
# Classical AI - Rule-Based Sentiment Analysis
# Uses IF-ELSE logic + word counting. Zero ML.
# ============================================================

from knowledge_base import POSITIVE_WORDS, NEGATIVE_WORDS
from preprocessor import preprocess


def analyze_sentiment(review_text):
    """
    Analyzes the sentiment of a review using rule-based word matching.

    Rules:
      IF positive_score > negative_score  → Positive
      IF negative_score > positive_score  → Negative
      ELSE                                → Neutral

    Returns:
      sentiment (str): "Positive", "Negative", or "Neutral"
      pos_score (int): count of positive words
      neg_score (int): count of negative words
    """

    tokens = preprocess(review_text)

    pos_score = 0
    neg_score = 0
    matched_positive = []
    matched_negative = []

    for word in tokens:
        if word in POSITIVE_WORDS:
            pos_score += 1
            matched_positive.append(word)
        elif word in NEGATIVE_WORDS:
            neg_score += 1
            matched_negative.append(word)

    # Rule-based decision
    if pos_score > neg_score:
        sentiment = "Positive"
    elif neg_score > pos_score:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "positive_score": pos_score,
        "negative_score": neg_score,
        "matched_positive": matched_positive,
        "matched_negative": matched_negative
    }


# Quick test
if __name__ == "__main__":
    reviews = [
        "This phone is excellent and battery life is amazing",
        "Terrible product, broken after one day, complete waste of money",
        "It is okay, nothing special"
    ]
    for r in reviews:
        result = analyze_sentiment(r)
        print(f"Review   : {r}")
        print(f"Sentiment: {result['sentiment']} | +{result['positive_score']} / -{result['negative_score']}")
        print()
