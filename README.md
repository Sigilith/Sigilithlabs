# Sigilithlabs

Sigilithlabs contains Sigilith-M, a structural analysis engine for symbolic sequences and comparative profile generation.

## What Sigilith-M does

Sigilith-M builds structured profiles from symbolic or tokenized input and supports:

- profile generation
- baseline comparison
- drift analysis
- stability scoring
- profile-to-profile comparison
- JSON export
- Markdown comparative reports

## Package layout

- `src/sigilith_m/metrics.py` - core sequence metrics
- `src/sigilith_m/drift.py` - drift and windowed drift
- `src/sigilith_m/baselines.py` - baseline families and observed-vs-baseline comparison
- `src/sigilith_m/classify.py` - summary classification rules
- `src/sigilith_m/profile.py` - canonical profile builder
- `src/sigilith_m/compare.py` - profile comparison engine
- `src/sigilith_m/report.py` - Markdown report generation
- `src/sigilith_m/export.py` - JSON-safe export helpers
- `src/sigilith_m/io.py` - file input/output helpers
- `src/sigilith_m/utils.py` - normalization and tokenization
- `src/sigilith_m/cli.py` - command-line interface

## Profile structure

A Sigilith-M profile includes:

- input text
- normalized text
- tokens
- metrics
- baseline profile
- metric deltas
- classification
- metadata

## Current metrics

Sigilith-M currently computes:

- score
- stability
- repetition ratio
- transition diversity
- drift
- normalized drift
- windowed drift
- stability index

## Baseline modes

Available baseline modes:

- `shuffle`
- `sorted`
- `local_shuffle`
- `block_shuffle`

## CLI usage

### Build a profile

PYTHONPATH=src python -m sigilith_m.cli profile input.txt output/profile.json

### Compare two inputs

PYTHONPATH=src python -m sigilith_m.cli compare input_a.txt input_b.txt output/compare.json

### Generate a Markdown report

PYTHONPATH=src python -m sigilith_m.cli report input_a.txt input_b.txt output/report.md

## CLI options

Common options:

- `--seed` - random seed for baseline generation
- `--baseline-mode` - choose baseline family
- `--window-size` - window size for local shuffle and windowed drift contexts
- `--block-size` - block size for block-preserving shuffle

Example:

PYTHONPATH=src python -m sigilith_m.cli report input_a.txt input_b.txt output/report.md --baseline-mode block_shuffle --block-size 4 --seed 7

## Comparison outputs

Sigilith-M comparative outputs currently include:

- Euclidean distance
- cosine similarity
- metric deltas across all tracked profile metrics

## Report generation

Sigilith-M can generate Markdown comparative reports containing:

- profile metadata
- profile metric tables
- comparison summary
- metric delta table

## Testing

Run the test suite with:

PYTHONPATH=src python -m pytest -v tests/unit

## Status

Current state of the engine:

- modular package structure
- canonical profile builder
- comparative engine
- multiple baseline families
- report generator
- CLI commands for profile, compare, and report
- passing unit tests

