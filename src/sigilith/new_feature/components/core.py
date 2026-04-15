"""
Core logic for the next Sigilith feature.
Implements a simple structural processing pipeline:
1. validate input
2. normalize input
3. extract structural tokens
4. compute a basic structural score
5. compute a stability score
6. compute a repetition ratio
7. compute transition diversity
8. assign a summary label
"""

from collections import Counter
from .utils import normalize, validate


class CoreEngine:
    def __init__(self):
        self.name = "NextFeatureEngine"

    def process(self, data):
        validated = validate(data)
        normalized = normalize(validated)
        tokens = self.extract_tokens(normalized)
        score = self.compute_score(tokens)
        stability = self.compute_stability(tokens)
        repetition_ratio = self.compute_repetition_ratio(tokens)
        transition_diversity = self.compute_transition_diversity(tokens)
        summary_label = self.compute_summary_label(
            stability=stability,
            repetition_ratio=repetition_ratio,
            transition_diversity=transition_diversity,
        )
        return {
            "normalized": normalized,
            "tokens": tokens,
            "score": score,
            "stability": stability,
            "repetition_ratio": repetition_ratio,
            "transition_diversity": transition_diversity,
            "summary_label": summary_label,
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

    def compute_stability(self, tokens):
        """
        Stability = frequency of the most common token divided by total tokens.
        Returns a value between 0 and 1.
        """
        if not tokens:
            return 0.0
        counts = Counter(tokens)
        most_common = counts.most_common(1)[0][1]
        return most_common / len(tokens)

    def compute_repetition_ratio(self, tokens):
        """
        Repetition ratio = repeated tokens / total tokens.
        """
        if not tokens:
            return 0.0
        total = len(tokens)
        unique = len(set(tokens))
        repeated = total - unique
        return repeated / total

    def compute_transition_diversity(self, tokens):
        """
        Transition diversity = unique adjacent transitions / total adjacent transitions.
        Returns a value between 0 and 1.
        """
        if len(tokens) < 2:
            return 0.0
        transitions = [(a, b) for a, b in zip(tokens, tokens[1:])]
        total = len(transitions)
        unique = len(set(transitions))
        return unique / total

    def compute_summary_label(self, stability, repetition_ratio, transition_diversity):
        """
        Simple summary classifier for the feature.
        """
        if stability >= 0.7 and repetition_ratio >= 0.4:
            return "high_repetition_stable"
        if transition_diversity >= 0.8 and stability < 0.7:
            return "high_transition_variability"
        if stability >= 0.4 and transition_diversity >= 0.4:
            return "balanced_structure"
        return "low_structure"
