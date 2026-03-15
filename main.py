# ============================================================
# main.py
# Product Review Analyzer - Classical AI Project
# Entry point: connects all modules together
# ============================================================

from input_handler import get_reviews
from sentiment_engine import analyze_sentiment
from fake_detector import detect_fake
from rating_calculator import calculate_genuine_rating


def print_separator(char="=", length=60):
    print(char * length)


def analyze_all_reviews(reviews):
    """
    Runs the full classical AI pipeline on each review:
      1. Sentiment Analysis (rule-based)
      2. Fake Detection (heuristic rules)
      3. Collects data for rating calculation
    """
    results = []

    print_separator()
    print("           REVIEW ANALYSIS RESULTS")
    print_separator()

    for i, review in enumerate(reviews, 1):
        text = review["review_text"]
        rating = review["rating"]

        # Step 1: Sentiment Analysis
        sentiment_result = analyze_sentiment(text)
        sentiment = sentiment_result["sentiment"]
        pos_score = sentiment_result["positive_score"]

        # Step 2: Fake Detection
        fake_result = detect_fake(text, rating, sentiment, pos_score)

        # Collect for rating calculation
        results.append({
            "rating": rating,
            "weight": fake_result["weight"],
            "label": fake_result["label"],
            "is_suspicious": fake_result["is_suspicious"]
        })

        # Print individual review report
        print(f"\nReview #{i}")
        print(f"  Text      : {text}")
        print(f"  Rating    : {'⭐' * rating} ({rating}/5)")
        print(f"  Sentiment : {sentiment} "
              f"(+{sentiment_result['positive_score']} pos / "
              f"-{sentiment_result['negative_score']} neg)")
        print(f"  Status    : {fake_result['label']} | Weight: {fake_result['weight']}")

        if fake_result["reasons"]:
            print("  ⚠ Suspicion Reasons:")
            for reason in fake_result["reasons"]:
                print(f"     - {reason}")

    return results


def print_final_report(rating_result):
    """Prints the final product rating summary."""
    print_separator()
    print("           FINAL PRODUCT RATING REPORT")
    print_separator()
    print(f"  Total Reviews Analyzed   : {rating_result['total_reviews']}")
    print(f"  Genuine Reviews          : {rating_result['genuine_count']}")
    print(f"  Slightly Suspicious      : {rating_result['slightly_suspicious_count']}")
    print(f"  Suspicious Reviews       : {rating_result['suspicious_count']}")
    print(f"  Raw Average Rating       : {rating_result['raw_average']} / 5.0")
    print(f"  ✅ Genuine AI Rating     : {rating_result['genuine_rating']} / 5.0")
    print(f"  📊 Recommendation        : {rating_result['recommendation']}")
    print_separator()

    genuine = rating_result['genuine_rating']
    full_stars = int(genuine)
    half = "½" if (genuine - full_stars) >= 0.5 else ""
    print(f"  Product Score: {'⭐' * full_stars}{half}  ({genuine}/5)")
    print_separator()


def main():
    print_separator()
    print("   PRODUCT REVIEW ANALYZER — Classical AI System")
    print("   Rule-Based | No Machine Learning | Python")
    print_separator()

    # Get reviews from user (manual / CSV / both)
    reviews = get_reviews()

    if not reviews:
        print("\n[ERROR] No reviews to analyze. Exiting.")
        return

    # Run full AI pipeline
    results = analyze_all_reviews(reviews)

    # Calculate genuine rating
    rating_result = calculate_genuine_rating(results)

    # Show final report
    print_final_report(rating_result)


if __name__ == "__main__":
    main()