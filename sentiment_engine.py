# ============================================================
# sentiment_engine.py
# Classical AI - Threshold-Based Sentiment Analysis
# Uses word scoring + threshold values instead of simple IF-ELSE
# ============================================================

from knowledge_base import POSITIVE_WORDS, NEGATIVE_WORDS
from preprocessor import preprocess
from thresholds import SENTIMENT_THRESHOLD


def analyze_sentiment(review_text):
    """
    Analyzes sentiment using threshold-based scoring.

    Logic:
      - Count positive and negative word matches
      - IF positive_score >= SENTIMENT_THRESHOLD
        AND positive_score > negative_score  → Positive
      - IF negative_score >= SENTIMENT_THRESHOLD
        AND negative_score > positive_score  → Negative
      - ELSE                                 → Neutral

    This is more precise than simple IF-ELSE because:
      - A review needs a minimum score to be classified
      - Weak reviews with only 1 matched word → Neutral
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

    # Threshold-based sentiment decision
    if pos_score >= SENTIMENT_THRESHOLD and pos_score > neg_score:
        sentiment = "Positive"
    elif neg_score >= SENTIMENT_THRESHOLD and neg_score > pos_score:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "positive_score": pos_score,
        "negative_score": neg_score,
        "matched_positive": matched_positive,
        "matched_negative": matched_negative,
        "sentiment_threshold_used": SENTIMENT_THRESHOLD
    }


# Quick test
if __name__ == "__main__":
    reviews = [
        "This phone is excellent and battery life is amazing and outstanding",
        "Terrible product broken after one day complete waste of money",
        "It is okay",
        "good product",
    ]
    for r in reviews:
        result = analyze_sentiment(r)
        print(f"Review    : {r}")
        print(f"Sentiment : {result['sentiment']} | +{result['positive_score']} / -{result['negative_score']} | Threshold: {result['sentiment_threshold_used']}")
        print()