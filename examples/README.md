# Examples

This directory contains **reference and experimental implementations** related to
the Ternary Logic Unit (TLU) semantics defined in `appendix.md`.

## Canonical Reference

- **`ternary_reference.py`**  
  Canonical, correctness-first software implementation of the TLU operations.
  This file serves as the **semantic oracle** for experiments, compilers, tests,
  and potential hardware implementations.

  All observable behavior must match this reference.

## Experimental Helpers

- **`ternary_numpy.py`**  
  Non-normative, experimental helpers built on top of `ternary_reference.py`
  using NumPy-style array operations. This file exists solely to support
  prototyping, vectorized experimentation, and exploratory evaluation.

  It must not be treated as a semantic reference.

## Notes

- Files in this directory are **not optimized**.
- None of the implementations are intended as production backends.
- Only `ternary_reference.py` defines authoritative semantics.

