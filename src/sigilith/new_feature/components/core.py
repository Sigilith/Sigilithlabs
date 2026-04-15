"""
Core logic for the next Sigilith feature.
Implements a simple structural processing pipeline:
1. validate input
2. normalize input
3. extract structural tokens
4. compute a basic structural score
"""

from .utils import normalize, validate


class CoreEngine:
    def __init__(self):
        self.name = "NextFeatureEngine"

    def process(self, data):
        validated = validate(data)
        normalized = normalize(validated)
        tokens = self.extract_tokens(normalized)
        score = self.compute_score(tokens)
        return {
            "normalized": normalized,
            "tokens": tokens,
            "score": score,
        }

    def extract_tokens(self, text):
        """Split into structural tokens."""
        return [t for t in text.split(" ") if t]

    def compute_score(self, tokens):
        """Basic scoring: total token count + uniqueness factor."""
        if not tokens:
            return 0
        unique = len(set(tokens))
        total = len(tokens)
        return total + unique
