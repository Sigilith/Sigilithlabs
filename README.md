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

### Alternate baseline mode

The CLI also supports a deterministic sorted baseline:

PYTHONPATH=src python -m sigilith_m.cli sample_input.txt output/profile.json --baseline-mode sorted

Available baseline modes:
- shuffle
- sorted

### Alternate baseline mode

The CLI also supports a deterministic sorted baseline:

PYTHONPATH=src python -m sigilith_m.cli sample_input.txt output/profile.json --baseline-mode sorted

Available baseline modes:
- shuffle
- sorted

### Alternate baseline mode

The CLI also supports a deterministic sorted baseline:

PYTHONPATH=src python -m sigilith_m.cli sample_input.txt output/profile.json --baseline-mode sorted

Available baseline modes:
- shuffle
- sorted

### Alternate baseline mode

The CLI also supports a deterministic sorted baseline:

PYTHONPATH=src python -m sigilith_m.cli sample_input.txt output/profile.json --baseline-mode sorted

Available baseline modes:
- shuffle
- sorted

### Alternate baseline mode

The CLI also supports a deterministic sorted baseline:


## Package Layout

Sigilith-M is currently organized into the following modules:

- `src/sigilith_m/metrics.py` — core sequence metrics
- `src/sigilith_m/drift.py` — drift calculations
- `src/sigilith_m/baselines.py` — baseline generation and comparison
- `src/sigilith_m/classify.py` — summary classification rules
- `src/sigilith_m/profile.py` — canonical profile builder
- `src/sigilith_m/export.py` — JSON-safe export helpers
- `src/sigilith_m/io.py` — file input/output helpers
- `src/sigilith_m/utils.py` — text normalization and tokenization
- `src/sigilith_m/cli.py` — command-line interface

## Profile Structure

Sigilith-M profiles currently include:

- input text
- normalized text
- tokens
- metrics
- baseline profile
- metric deltas
- classification
- metadata
