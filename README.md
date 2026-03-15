# Product Review Analyzer

Rule-based Classical AI project for analyzing product reviews, identifying suspicious feedback, and computing a corrected product rating.

## Features

- Threshold-based sentiment analysis with `Positive`, `Negative`, and `Neutral` labels
- Heuristic fake-review detection with three trust levels:
  - `Genuine`
  - `Slightly Suspicious`
  - `Suspicious`
- Weighted "Genuine AI Rating" that reduces the impact of suspicious reviews
- Two entry points:
  - CLI workflow in `main.py`
  - Flask web app in `web_app.py`
- Explainable results, including matched sentiment words, suspicion score, and triggered rules

## Current Pipeline

1. `preprocessor.py` cleans the review text by lowercasing, removing punctuation, tokenizing, and removing stopwords.
2. `sentiment_engine.py` counts dictionary matches from `knowledge_base.py` and applies `SENTIMENT_THRESHOLD` from `thresholds.py`.
3. `fake_detector.py` applies six heuristic rules and assigns a suspicion score, label, and weight.
4. `rating_calculator.py` computes:
   - Raw average rating
   - Genuine AI Rating
   - Review counts by trust level
   - Recommendation label

## Thresholds and Weights

Defined in `thresholds.py`:

- `SENTIMENT_THRESHOLD = 2`
- `WORD_COUNT_THRESHOLD = 5`
- `POSITIVITY_THRESHOLD = 4`
- `SUSPICION_LEVEL_1 = 1`
- `SUSPICION_LEVEL_2 = 2`
- `WEIGHT_GENUINE = 1.0`
- `WEIGHT_SLIGHTLY_SUSPICIOUS = 0.7`
- `WEIGHT_SUSPICIOUS = 0.4`
- `RATING_HIGHLY_RECOMMENDED = 4.0`
- `RATING_RECOMMENDED = 3.0`

## Suspicion Rules

`fake_detector.py` flags reviews using these rules:

- `R1`: Short review with a high star rating
- `R2`: Negative sentiment with a 4 or 5 star rating
- `R3`: Positive sentiment with a 1 or 2 star rating
- `R4`: Contains known suspicious phrases
- `R5`: Overly positive language with a 5-star rating
- `R6`: Neutral sentiment with an extreme rating of 1 or 5

## Project Structure

- `main.py` - CLI entry point and report output
- `web_app.py` - Flask app with manual input and CSV upload
- `input_handler.py` - CLI input collection
- `preprocessor.py` - text cleaning and tokenization
- `knowledge_base.py` - sentiment words, suspicious phrases, and stopwords
- `sentiment_engine.py` - threshold-based sentiment scoring
- `fake_detector.py` - heuristic suspicious review detection
- `rating_calculator.py` - weighted rating and recommendation
- `thresholds.py` - centralized thresholds and weights
- `templates/index.html` - web interface
- `static/style.css` - web styling
- `reviews.csv` - sample dataset

## Setup

1. Install Python 3.
2. Install Flask:

```bash
pip install flask
```

## Run the CLI Version

```bash
python main.py
```

CLI modes:

- Manual review entry
- CSV loading
- Combined CSV + manual entry

## Run the Web Version

```bash
python web_app.py
```

Then open `http://127.0.0.1:5000`.

## Input Formats

### Manual input

One review per line:

```text
rating|review text
```

Example:

```text
5|Excellent battery life and smooth performance
1|Worst purchase, very bad quality
```

### CSV input

Required headers:

```text
review_text,rating
```

Example:

```csv
review_text,rating
"Excellent camera and fast charging",5
"Terrible quality, stopped working",1
```

## Output

For each review, the system can report:

- Star rating
- Sentiment label and positive/negative scores
- Matched positive and negative words
- Suspicion score
- Trust label
- Applied weight
- Triggered suspicion reasons

Final summary includes:

- Total reviews
- Genuine review count
- Slightly suspicious review count
- Suspicious review count
- Raw average rating
- Genuine AI Rating
- Recommendation label

## Notes

- This project is fully rule-based; it does not train or use a machine learning model.
- The web app validates manual input and uploaded CSV data before analysis.
- Ratings must be integers from 1 to 5.
