# ============================================================
# fake_detector.py
# Classical AI - Threshold-Based Fake Review Detection
# Uses heuristic rules + suspicion scoring with thresholds
# ============================================================

from knowledge_base import SUSPICIOUS_PHRASES, POSITIVE_WORDS
from preprocessor import preprocess
from thresholds import (
    WORD_COUNT_THRESHOLD, POSITIVITY_THRESHOLD,
    SUSPICION_LEVEL_1, SUSPICION_LEVEL_2,
    WEIGHT_GENUINE, WEIGHT_SLIGHTLY_SUSPICIOUS, WEIGHT_SUSPICIOUS
)


def detect_fake(review_text, star_rating, sentiment, pos_score):
    """
    Detects whether a review is genuine or suspicious using
    heuristic rules and threshold-based suspicion scoring.

    Rules Applied:
      R1: Word count < WORD_COUNT_THRESHOLD + high rating (4-5) → +1 suspicion
      R2: Sentiment is Negative BUT rating is 4 or 5            → +1 suspicion
      R3: Sentiment is Positive BUT rating is 1 or 2            → +1 suspicion
      R4: Review contains known suspicious phrases               → +1 suspicion
      R5: Positive score >= POSITIVITY_THRESHOLD + 5 stars      → +1 suspicion
      R6: Neutral sentiment + extreme rating (1 or 5)            → +1 suspicion

    Suspicion Level (threshold-based):
      0 rules triggered → Genuine            (Weight = 1.0)
      1 rule  triggered → Slightly Suspicious (Weight = 0.7)
      2+ rules triggered → Suspicious         (Weight = 0.4)
    """

    tokens = preprocess(review_text)
    word_count = len(tokens)
    suspicion_score = 0
    reasons = []
    text_lower = review_text.lower()

    # R1: Below word count threshold + high rating
    if word_count < WORD_COUNT_THRESHOLD and star_rating >= 4:
        suspicion_score += 1
        reasons.append(f"R1: Review too short (words: {word_count} < threshold: {WORD_COUNT_THRESHOLD}) with high rating")

    # R2: Negative sentiment but high star rating
    if sentiment == "Negative" and star_rating >= 4:
        suspicion_score += 1
        reasons.append("R2: Negative sentiment but high star rating")

    # R3: Positive sentiment but low star rating
    if sentiment == "Positive" and star_rating <= 2:
        suspicion_score += 1
        reasons.append("R3: Positive sentiment but low star rating")

    # R4: Contains suspicious phrases
    for phrase in SUSPICIOUS_PHRASES:
        if phrase in text_lower:
            suspicion_score += 1
            reasons.append(f"R4: Contains suspicious phrase → '{phrase}'")
            break

    # R5: Overly positive score beyond threshold + 5 stars
    if pos_score >= POSITIVITY_THRESHOLD and star_rating == 5:
        suspicion_score += 1
        reasons.append(f"R5: Overly positive score ({pos_score} >= threshold: {POSITIVITY_THRESHOLD}) with 5-star rating")

    # R6: Neutral sentiment + extreme rating
    if sentiment == "Neutral" and star_rating in [1, 5]:
        suspicion_score += 1
        reasons.append("R6: Neutral sentiment with extreme star rating")

    # Threshold-based label and weight assignment
    if suspicion_score == 0:
        label = "Genuine"
        weight = WEIGHT_GENUINE
    elif suspicion_score == SUSPICION_LEVEL_1:
        label = "Slightly Suspicious"
        weight = WEIGHT_SLIGHTLY_SUSPICIOUS
    else:
        label = "Suspicious"
        weight = WEIGHT_SUSPICIOUS

    is_suspicious = suspicion_score >= SUSPICION_LEVEL_1

    return {
        "is_suspicious": is_suspicious,
        "label": label,
        "suspicion_score": suspicion_score,
        "reasons": reasons,
        "weight": weight
    }


# Quick test
if __name__ == "__main__":
    tests = [
        ("This phone is excellent and battery life is amazing", 5, "Positive", 2),
        ("Terrible product broken waste of money", 5, "Negative", 0),
        ("ok", 5, "Neutral", 0),
        ("best ever must buy changed my life", 5, "Positive", 2),
        ("good", 4, "Neutral", 1),
    ]
    for text, rating, sentiment, pos in tests:
        result = detect_fake(text, rating, sentiment, pos)
        print(f"Review         : {text}")
        print(f"Label          : {result['label']} | Suspicion Score: {result['suspicion_score']} | Weight: {result['weight']}")
        if result['reasons']:
            for r in result['reasons']:
                print(f"  ⚠ {r}")
        print()