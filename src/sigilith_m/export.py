import json
from pathlib import Path


def to_dict(profile):
    """
    Ensure the profile is JSON-safe.
    """
    if isinstance(profile, dict):
        result = {}
        for key, value in profile.items():
            if isinstance(value, dict):
                result[key] = to_dict(value)
            elif isinstance(value, (list, tuple)):
                result[key] = [
                    to_dict(v) if isinstance(v, dict) else list(v) if isinstance(v, tuple) else v
                    for v in value
                ]
            else:
                result[key] = value
        return result
    return profile


def save_json(profile, path):
    """
    Save a structural profile to JSON.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    safe_profile = to_dict(profile)

    with path.open("w", encoding="utf-8") as f:
        json.dump(safe_profile, f, indent=2, ensure_ascii=False)

    return str(path)
