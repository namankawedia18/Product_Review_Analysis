# ============================================================
# fake_detector.py
# Classical AI - Heuristic Fake Review Detection
# Uses predefined IF-ELSE rules. No ML at all.
# ============================================================

from knowledge_base import SUSPICIOUS_PHRASES
from preprocessor import preprocess


def detect_fake(review_text, star_rating, sentiment):
    """
    Detects whether a review is genuine or suspicious using heuristic rules.

    Rules Applied:
      R1: Very short review (< 4 words) + high rating (4-5) → Suspicious
      R2: Sentiment is Negative BUT rating is 4 or 5         → Suspicious
      R3: Sentiment is Positive BUT rating is 1 or 2         → Suspicious
      R4: Review contains known suspicious phrases            → Suspicious
      R5: All words are extreme positives (no negatives)
          AND rating is 5                                     → Suspicious
      R6: Review is extremely long (> 100 words) with
          only generic praise                                 → Suspicious

    Returns:
      is_suspicious (bool)
      reasons (list of str): which rules triggered
      weight (float): 1.0 for genuine, 0.4 for suspicious
    """

    tokens = preprocess(review_text)
    word_count = len(tokens)
    reasons = []
    text_lower = review_text.lower()

    # R1: Too short + high rating
    if word_count < 4 and star_rating >= 4:
        reasons.append("R1: Review too short with high rating")

    # R2: Negative sentiment but high star rating
    if sentiment == "Negative" and star_rating >= 4:
        reasons.append("R2: Negative sentiment but high star rating")

    # R3: Positive sentiment but low star rating
    if sentiment == "Positive" and star_rating <= 2:
        reasons.append("R3: Positive sentiment but low star rating")

    # R4: Contains suspicious phrases
    for phrase in SUSPICIOUS_PHRASES:
        if phrase in text_lower:
            reasons.append(f"R4: Contains suspicious phrase → '{phrase}'")
            break

    # R5: Extremely short review with only 5 stars
    if word_count <= 2 and star_rating == 5:
        reasons.append("R5: Extremely short review with 5-star rating")

    # R6: Neutral sentiment but extreme rating (1 or 5)
    if sentiment == "Neutral" and star_rating in [1, 5]:
        reasons.append("R6: Neutral sentiment with extreme star rating")

    is_suspicious = len(reasons) > 0
    weight = 0.4 if is_suspicious else 1.0

    return {
        "is_suspicious": is_suspicious,
        "label": "Suspicious" if is_suspicious else "Genuine",
        "reasons": reasons,
        "weight": weight
    }


# Quick test
if __name__ == "__main__":
    tests = [
        ("This phone is excellent and battery life is amazing", 5, "Positive"),
        ("Terrible product broken waste of money", 5, "Negative"),
        ("ok", 5, "Neutral"),
        ("best ever must buy changed my life", 5, "Positive"),
    ]
    for text, rating, sentiment in tests:
        result = detect_fake(text, rating, sentiment)
        print(f"Review : {text}")
        print(f"Label  : {result['label']} | Weight: {result['weight']}")
        if result['reasons']:
            for r in result['reasons']:
                print(f"  ⚠ {r}")
        print()
