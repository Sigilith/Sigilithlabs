# Sigilith Labs

Sigilith Labs is an independent research initiative focused on structural intelligence for symbolic systems.

We develop structural methods, computational tools, and analytical outputs for manuscripts, symbolic datasets, and constrained pattern systems. Our work is grounded in reproducible, domain‑agnostic structural analysis.

---

## Structure of the Sigilith Ecosystem

### **Sigilith (Framework)**
The structural methodology defining the metrics, laws, and analytical approach used to classify symbolic systems.

### **Sigilith‑M (Engine)**
The computational engine used within the Sigilith Labs research pipeline.  
It applies the Sigilith framework to sequences by extracting structural metrics, generating terrain vectors, and supporting comparative analysis.

### **Sigilith Reports**
Fixed‑price applied analyses for manuscripts, symbolic datasets, and pattern‑constrained systems.

### **Sigilith Consulting**
Bespoke structural intelligence for researchers, institutions, archives, labs, and specialist clients.

---

## What Sigilith Labs Does

Sigilith Labs studies how symbolic systems behave.  
We analyse how symbols cluster, drift, stabilise, and separate into measurable regimes using structural metrics such as:

- adjacency entropy  
- boundary concentration  
- drift  
- stability  
- phase‑space projection  

Our work is non‑linguistic, non‑semantic, and fully structural.

---

## Publications

Selected work includes:

- **Structural Classification of Symbolic Systems**  
- **The Harmonica Test**  
- **Voynich Manuscript Analysis**  

A full bibliography is available on request.

---

## Contact

For collaboration, reports, or research inquiries:

**kynash1@outlook.com**


## New Feature Module

A new structural processing feature has been added to the Sigilith codebase.

### Current capabilities
- input validation
- normalization
- structural token extraction
- score metric
- stability metric
- repetition ratio metric
- transition diversity metric
- summary label classification

### Output fields
The feature currently returns:
- `normalized`
- `tokens`
- `score`
- `stability`
- `repetition_ratio`
- `transition_diversity`
- `summary_label`

### Status
This module is implemented, tested, and merged into `main`.

### Test coverage
Current tests verify:
- valid structural processing
- rejection of `None` input
- normalization behavior
- transition-based metric behavior


## New Feature Module

A new structural processing feature has been added to the Sigilith codebase.

### Current capabilities
- input validation
- normalization
- structural token extraction
- score metric
- stability metric
- repetition ratio metric
- transition diversity metric
- summary label classification

### Output fields
The feature currently returns:
- `normalized`
- `tokens`
- `score`
- `stability`
- `repetition_ratio`
- `transition_diversity`
- `summary_label`

### Status
This module is implemented, tested, and merged into `main`.

### Test coverage
Current tests verify:
- valid structural processing
- rejection of `None` input
- normalization behavior
- transition-based metric behavior

## New Feature Module

A new structural processing feature has been added to the Sigilith codebase.

### Current capabilities
- input validation
- normalization
- structural token extraction
- score metric
- stability metric
- repetition ratio metric
- transition diversity metric
- summary label classification

### Output fields
The feature currently returns:
- `normalized`
- `tokens`
- `score`
- `stability`
- `repetition_ratio`
- `transition_diversity`
- `summary_label`

### Status
This module is implemented, tested, and merged into `main`.

### Test coverage
Current tests verify:
- valid structural processing
- rejection of `None` input
- normalization behavior
- transition-based metric behavior
## New Feature Module

A new structural processing feature has been added to the Sigilith codebase.

### Current capabilities
- input validation
- normalization
- structural token extraction
- score metric
- stability metric
- repetition ratio metric
- transition diversity metric
- summary label classification

### Output fields
The feature currently returns:
- `normalized`
- `tokens`
- `score`
- `stability`
- `repetition_ratio`
- `transition_diversity`
- `summary_label`

### Status
This module is implemented, tested, and merged into `main`.

### Test coverage
Current tests verify:
- valid structural processing
- rejection of `None` input
- normalization behavior
- transition-based metric behavior

## Sigilith-M CLI

Sigilith-M includes a command-line interface for generating structural profiles from text input and exporting them as JSON.

### Example usage

```bash
PYTHONPATH=src python -m sigilith_m.cli sample_input.txt output/profile.json
### Current CLI output includes
- normalized text
- token list
- score
- stability
- repetition ratio
- transition diversity
- summary label
- shuffled baseline profile
- metric deltas against baseline

### Baseline comparison
The CLI now supports comparison between an observed token profile and a shuffled baseline, allowing structural deltas to be inspected directly in exported JSON output.

### Alternate baseline mode

The CLI also supports a deterministic sorted baseline:

```bash
PYTHONPATH=src python -m sigilith_m.cli sample_input.txt output/profile.json --baseline-mode sorted

cat >> README.md <<'EOF'

### Alternate baseline mode

The CLI also supports a deterministic sorted baseline:

```bash
PYTHONPATH=src python -m sigilith_m.cli sample_input.txt output/profile.json --baseline-mode sorted

Then save it:

```bash
git add README.md
git commit -m "Document sorted baseline mode in README"
git push
cat > tests/unit/test_cli.py <<'EOF'
from sigilith_m.cli import build_profile_from_text


def test_build_profile_from_text():
    result = build_profile_from_text("HELLO world hello", seed=42, baseline_mode="shuffle")

    assert result["normalized"] == "hello world hello"
    assert result["tokens"] == ["hello", "world", "hello"]
    assert result["score"] == 5
    assert result["stability"] == 2 / 3
    assert result["repetition_ratio"] == 1 / 3
    assert result["transition_diversity"] == 1.0
    assert result["drift"] == 2.0
    assert result["normalized_drift"] == 1.0
    assert result["summary_label"] == "high_transition_variability"
    assert result["seed"] == 42
    assert result["baseline_mode"] == "shuffle"

    assert "baseline" in result
    assert "deltas" in result
    assert "score_delta" in result["deltas"]
    assert "drift_delta" in result["deltas"]


def test_build_profile_with_sorted_baseline():
    result = build_profile_from_text("b a c a", baseline_mode="sorted")

    assert result["baseline_mode"] == "sorted"
    assert result["baseline"]["tokens"] == ["a", "a", "b", "c"]
