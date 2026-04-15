# Sigilithlabs

Sigilithlabs is a structural analysis codebase for symbolic systems, sequence behaviour, and reproducible metric-based experimentation.

## Current components

### New Feature Module
A structural processing feature has been added to the codebase.

Current capabilities:
- input validation
- normalization
- structural token extraction
- score metric
- stability metric
- repetition ratio metric
- transition diversity metric
- summary label classification

Current output fields:
- normalized
- tokens
- score
- stability
- repetition_ratio
- transition_diversity
- summary_label

### Sigilith-M export support
Sigilith-M now supports JSON export for structural profiles.

### Sigilith-M CLI
Sigilith-M includes a command-line interface for generating structural profiles from text input and exporting them as JSON.

Example usage:

PYTHONPATH=src python -m sigilith_m.cli sample_input.txt output/profile.json

Current CLI output includes:
- normalized text
- token list
- score
- stability
- repetition ratio
- transition diversity
- drift
- normalized drift
- summary label
- shuffled baseline profile
- metric deltas against baseline

### Alternate baseline mode
The CLI also supports a deterministic sorted baseline:

PYTHONPATH=src python -m sigilith_m.cli sample_input.txt output/profile.json --baseline-mode sorted

Available baseline modes:
- shuffle
- sorted

## Status
The current codebase includes:
- tested feature modules
- JSON export support
- CLI profile generation
- baseline comparison
- sorted baseline mode
- drift support
- unit tests for key modules
