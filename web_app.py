import csv
import io

from flask import Flask, render_template, request

from fake_detector import detect_fake
from rating_calculator import calculate_genuine_rating
from sentiment_engine import analyze_sentiment

app = Flask(__name__)


def parse_manual_reviews(raw_text):
    """
    Expected manual format per line:
      rating|review text
    Example:
      5|Excellent battery life
      1|Worst product ever
    """
    reviews = []
    errors = []

    if not raw_text.strip():
        return reviews, errors

    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

    for idx, line in enumerate(lines, start=1):
        if "|" not in line:
            errors.append(f"Line {idx}: Missing '|' separator.")
            continue

        rating_part, review_part = line.split("|", 1)
        rating_part = rating_part.strip()
        review_part = review_part.strip()

        try:
            rating = int(rating_part)
        except ValueError:
            errors.append(f"Line {idx}: Rating must be a number from 1 to 5.")
            continue

        if rating < 1 or rating > 5:
            errors.append(f"Line {idx}: Rating must be between 1 and 5.")
            continue

        if not review_part:
            errors.append(f"Line {idx}: Review text is empty.")
            continue

        reviews.append({"review_text": review_part, "rating": rating})

    return reviews, errors


def parse_csv_reviews(file_bytes):
    reviews = []
    errors = []

    try:
        content = file_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return reviews, ["CSV file must be UTF-8 encoded."]

    reader = csv.DictReader(io.StringIO(content))
    required = {"review_text", "rating"}
    fieldnames = set(reader.fieldnames or [])

    if not required.issubset(fieldnames):
        return reviews, ["CSV must contain headers: review_text,rating"]

    for idx, row in enumerate(reader, start=2):
        review_text = (row.get("review_text") or "").strip()
        rating_raw = (row.get("rating") or "").strip()

        try:
            rating = int(rating_raw)
        except ValueError:
            errors.append(f"CSV line {idx}: Rating must be a number.")
            continue

        if rating < 1 or rating > 5:
            errors.append(f"CSV line {idx}: Rating must be between 1 and 5.")
            continue

        if not review_text:
            errors.append(f"CSV line {idx}: Review text is empty.")
            continue

        reviews.append({"review_text": review_text, "rating": rating})

    return reviews, errors


def run_pipeline(reviews):
    detailed_results = []
    calculation_input = []

    for review in reviews:
        text = review["review_text"]
        rating = review["rating"]

        sentiment_result = analyze_sentiment(text)
        fake_result = detect_fake(text, rating, sentiment_result["sentiment"])

        detailed_results.append(
            {
                "review_text": text,
                "rating": rating,
                "sentiment": sentiment_result["sentiment"],
                "positive_score": sentiment_result["positive_score"],
                "negative_score": sentiment_result["negative_score"],
                "matched_positive": sentiment_result["matched_positive"],
                "matched_negative": sentiment_result["matched_negative"],
                "label": fake_result["label"],
                "weight": fake_result["weight"],
                "reasons": fake_result["reasons"],
            }
        )

        calculation_input.append(
            {
                "rating": rating,
                "weight": fake_result["weight"],
                "is_suspicious": fake_result["is_suspicious"],
            }
        )

    summary = calculate_genuine_rating(calculation_input)
    return detailed_results, summary


@app.route("/", methods=["GET", "POST"])
def index():
    detailed_results = []
    summary = None
    errors = []
    source_mode = "manual"

    if request.method == "POST":
        source_mode = request.form.get("source_mode", "manual")
        reviews = []

        if source_mode == "manual":
            manual_text = request.form.get("manual_reviews", "")
            reviews, parse_errors = parse_manual_reviews(manual_text)
            errors.extend(parse_errors)
        elif source_mode == "csv":
            csv_file = request.files.get("csv_file")
            if not csv_file or not csv_file.filename:
                errors.append("Please choose a CSV file.")
            else:
                csv_reviews, csv_errors = parse_csv_reviews(csv_file.read())
                reviews.extend(csv_reviews)
                errors.extend(csv_errors)
        else:
            errors.append("Invalid input mode selected.")

        if not errors and reviews:
            detailed_results, summary = run_pipeline(reviews)
        elif not errors and not reviews:
            errors.append("No valid reviews found to analyze.")

    return render_template(
        "index.html",
        detailed_results=detailed_results,
        summary=summary,
        errors=errors,
        source_mode=source_mode,
    )


if __name__ == "__main__":
    app.run(debug=True)
