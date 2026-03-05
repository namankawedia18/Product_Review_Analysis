# ============================================================
# rating_calculator.py
# Classical AI - Genuine Rating Calculator
# Uses weighted average formula. Pure logic, no ML.
# ============================================================


def calculate_genuine_rating(reviews_data):
    """
    Calculates a corrected product rating by giving less weight
    to suspicious reviews.

    Formula:
      Genuine Rating = Sum(rating × weight) / Sum(weights)

    Args:
      reviews_data: list of dicts, each containing:
        - 'rating'  (int 1-5)
        - 'weight'  (float: 1.0 for genuine, 0.4 for suspicious)

    Returns:
      genuine_rating (float): rounded to 2 decimal places
      raw_average    (float): simple average ignoring suspicion
      total_reviews  (int)
      genuine_count  (int)
      suspicious_count (int)
    """

    if not reviews_data:
        return None

    total_weighted = 0.0
    total_weights = 0.0
    total_raw = 0.0
    genuine_count = 0
    suspicious_count = 0

    for review in reviews_data:
        rating = review["rating"]
        weight = review["weight"]
        is_suspicious = review["is_suspicious"]

        total_weighted += rating * weight
        total_weights += weight
        total_raw += rating

        if is_suspicious:
            suspicious_count += 1
        else:
            genuine_count += 1

    genuine_rating = round(total_weighted / total_weights, 2) if total_weights > 0 else 0
    raw_average = round(total_raw / len(reviews_data), 2)
    total_reviews = len(reviews_data)

    return {
        "genuine_rating": genuine_rating,
        "raw_average": raw_average,
        "total_reviews": total_reviews,
        "genuine_count": genuine_count,
        "suspicious_count": suspicious_count
    }
