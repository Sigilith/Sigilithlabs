"""
Utility helpers for the next Sigilith feature.
"""

def validate(data):
    if data is None:
        raise ValueError("Input cannot be None")
    return data

def normalize(data):
    if isinstance(data, str):
        return data.strip().lower()
    return data
