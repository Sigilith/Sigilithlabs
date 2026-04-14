"""
Core logic for the next Sigilith feature.
This module defines the primary processing pipeline.
"""

from .utils import normalize, validate


class CoreEngine:
    def __init__(self):
        self.name = "NextFeatureEngine"

    def process(self, data):
        validated = validate(data)
        return normalize(validated)
