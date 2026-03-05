# ============================================================
# knowledge_base.py
# Classical AI - Knowledge Base (Word Dictionaries)
# This is the "brain" of the system — no ML, just rules!
# ============================================================

# Words that indicate a POSITIVE sentiment
POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "awesome", "fantastic",
    "wonderful", "best", "love", "perfect", "outstanding", "superb",
    "brilliant", "impressive", "satisfied", "happy", "worth", "durable",
    "reliable", "recommend", "quality", "nice", "solid", "smooth",
    "fast", "efficient", "beautiful", "elegant", "helpful", "friendly"
}

# Words that indicate a NEGATIVE sentiment
NEGATIVE_WORDS = {
    "bad", "poor", "worst", "terrible", "horrible", "awful",
    "useless", "broken", "waste", "disappointed", "cheap", "slow",
    "ugly", "defective", "damaged", "faulty", "unreliable", "pathetic",
    "frustrating", "annoying", "regret", "return", "refund", "fake",
    "misleading", "overpriced", "dirty", "noisy", "fragile", "weak"
}

# Phrases or words that may indicate a FAKE or SUSPICIOUS review
SUSPICIOUS_PHRASES = {
    "must buy", "best ever", "highly recommend everyone", "perfect in every way",
    "no complaints at all", "absolutely perfect", "100% satisfied",
    "buy this now", "do not miss", "changed my life"
}

# Common stopwords to remove during preprocessing
STOPWORDS = {
    "i", "me", "my", "we", "our", "you", "your", "he", "she", "it",
    "they", "them", "the", "a", "an", "and", "or", "but", "in", "on",
    "at", "to", "for", "of", "with", "is", "was", "are", "were", "be",
    "been", "being", "have", "has", "had", "do", "does", "did", "will",
    "would", "could", "should", "not", "no", "so", "if", "this", "that",
    "these", "those", "it", "its", "very", "just", "also", "then", "than"
}
