"""
Utility helpers for the next Sigilith feature.
"""

def validate(data):
    if data is None:
        raise ValueError("Input cannot be None")
    if not isinstance(data, (str, int, float)):
        raise TypeError("Unsupported data type")
    return data


def normalize(data):
    if isinstance(data, str):
        return data.strip().lower()
    return str(data)
