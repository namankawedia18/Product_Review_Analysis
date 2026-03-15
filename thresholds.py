# ============================================================
# thresholds.py
# Classical AI - Centralized Threshold Configuration
# All threshold values are defined here in one place.
# Change values here to tune the entire system.
# ============================================================

# ── Sentiment Analysis Thresholds ───────────────────────────
# Minimum score required to classify as Positive or Negative
# If both scores are below this, review is classified as Neutral
SENTIMENT_THRESHOLD = 2

# ── Fake Detection Thresholds ────────────────────────────────
# Minimum word count a review must have to be considered detailed
WORD_COUNT_THRESHOLD = 5

# Maximum positive score allowed before flagging as overly positive
POSITIVITY_THRESHOLD = 4

# Number of rules triggered to determine suspicion level:
#   0 rules  → Genuine
#   1 rule   → Slightly Suspicious
#   2+ rules → Suspicious
SUSPICION_LEVEL_1 = 1   # Slightly Suspicious
SUSPICION_LEVEL_2 = 2   # Suspicious

# ── Weight Thresholds ────────────────────────────────────────
# Weight assigned based on suspicion level
WEIGHT_GENUINE            = 1.0   # 0 rules triggered
WEIGHT_SLIGHTLY_SUSPICIOUS = 0.7  # 1 rule triggered
WEIGHT_SUSPICIOUS          = 0.4  # 2 or more rules triggered

# ── Final Rating Thresholds ──────────────────────────────────
# Used to give a recommendation label based on genuine rating
RATING_HIGHLY_RECOMMENDED = 4.0   # >= 4.0 → Highly Recommended
RATING_RECOMMENDED        = 3.0   # >= 3.0 → Recommended
                                   # <  3.0 → Not Recommended
