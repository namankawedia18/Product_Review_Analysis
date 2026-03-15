# ============================================================
# rating_calculator.py
# Classical AI - Genuine Rating Calculator with Threshold Labels
# Uses weighted average formula + threshold-based recommendation
# ============================================================

from thresholds import RATING_HIGHLY_RECOMMENDED, RATING_RECOMMENDED


def calculate_genuine_rating(reviews_data):
    """
    Calculates a corrected product rating using weighted average.

    Formula:
      Genuine Rating = Sum(rating × weight) / Sum(weights)

    Threshold-based Recommendation:
      >= 4.0 → Highly Recommended
      >= 3.0 → Recommended
      <  3.0 → Not Recommended
    """

    if not reviews_data:
        return None

    total_weighted = 0.0
    total_weights = 0.0
    total_raw = 0.0
    genuine_count = 0
    slightly_suspicious_count = 0
    suspicious_count = 0

    for review in reviews_data:
        rating = review["rating"]
        weight = review["weight"]
        label = review["label"]

        total_weighted += rating * weight
        total_weights += weight
        total_raw += rating

        if label == "Genuine":
            genuine_count += 1
        elif label == "Slightly Suspicious":
            slightly_suspicious_count += 1
        else:
            suspicious_count += 1

    genuine_rating = round(total_weighted / total_weights, 2) if total_weights > 0 else 0
    raw_average = round(total_raw / len(reviews_data), 2)
    total_reviews = len(reviews_data)

    # Threshold-based recommendation label
    if genuine_rating >= RATING_HIGHLY_RECOMMENDED:
        recommendation = "⭐ Highly Recommended"
    elif genuine_rating >= RATING_RECOMMENDED:
        recommendation = "👍 Recommended"
    else:
        recommendation = "👎 Not Recommended"

    return {
        "genuine_rating": genuine_rating,
        "raw_average": raw_average,
        "total_reviews": total_reviews,
        "genuine_count": genuine_count,
        "slightly_suspicious_count": slightly_suspicious_count,
        "suspicious_count": suspicious_count,
        "recommendation": recommendation
    }