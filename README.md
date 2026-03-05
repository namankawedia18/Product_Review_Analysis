# Product Review Analyzer

A rule-based **Classical AI** project that analyzes product reviews, detects suspicious/fake patterns, and computes a corrected product rating.

## What It Does

- Performs sentiment analysis using a dictionary-based approach (`Positive`, `Negative`, `Neutral`)
- Flags suspicious reviews using heuristic IF-ELSE rules
- Calculates a **Genuine AI Rating** using weighted averaging
- Supports both:
  - CLI mode (`main.py`)
  - Web mode with Flask (`web_app.py`)

## Tech Stack

- Python 3
- Flask (for web interface)
- CSV input support (`review_text`, `rating`)

## Project Structure

- `main.py` - CLI entry point
- `web_app.py` - Flask web app entry point
- `input_handler.py` - Manual/CSV input handling (CLI)
- `preprocessor.py` - Text cleaning and tokenization
- `knowledge_base.py` - Positive/negative words, suspicious phrases, stopwords
- `sentiment_engine.py` - Rule-based sentiment analysis
- `fake_detector.py` - Heuristic suspicious review detection
- `rating_calculator.py` - Weighted genuine rating computation
- `templates/index.html` - Web UI template
- `static/style.css` - Web UI styling
- `reviews.csv` - Example CSV data

## Setup

1. Ensure Python 3 is installed.
2. Install Flask:

```bash
pip install flask
```

## Run the CLI Version

```bash
python main.py
```

CLI supports:

- Manual review entry
- CSV file loading
- Combined manual + CSV input

## Run the Web Version

```bash
python web_app.py
```

Then open:

- `http://127.0.0.1:5000`

## Input Format

### Option 1: Manual Input (Web)

One review per line in this format:

```text
rating|review text
```

Example:

```text
5|Excellent battery life and smooth performance
1|Worst purchase, very bad quality
```

### Option 2: CSV Upload

CSV must contain headers:

```text
review_text,rating
```

Example:

```csv
review_text,rating
"Excellent camera and fast charging",5
"Terrible quality, stopped working",1
```

## Scoring Logic

- Genuine review weight: `1.0`
- Suspicious review weight: `0.4`

Final rating formula:

```text
Genuine Rating = Sum(rating * weight) / Sum(weights)
```

## Output Includes

- Per-review sentiment and suspicion label
- Triggered suspicion reasons (if any)
- Raw average rating
- Genuine AI Rating
- Counts of genuine vs suspicious reviews

## Notes

- This project uses **rule-based AI** only (no machine learning model).
- Review validation enforces rating range from 1 to 5.
