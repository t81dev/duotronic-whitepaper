# Conformance and Correctness

This document defines the conformance expectations for implementations that claim to support the **Ternary Logic Unit (TLU)** semantics described in this repository.

The goal of conformance is **semantic correctness**, not performance, encoding choice, or hardware capability.

---

## 1. Scope of Conformance

An implementation is considered *TLU-conformant* if it faithfully implements the **normative semantics** defined in:

* `appendix.md` — *Formal Semantics and Reference Material*

Conformance applies to:

* software libraries
* compiler intrinsics or lowering passes
* emulators or simulators
* hardware implementations (partial or complete)

Conformance does **not** require any specific performance characteristics, instruction encodings, or vector widths.

---

## 2. Normative Semantic Reference

The authoritative executable reference for TLU semantics is:

* `examples/ternary_reference.py`

All conformant implementations must produce results **observationally equivalent** to this reference for the operations they claim to support.

Where discrepancies arise between prose and code, the **appendix.md definitions take precedence**, followed by the reference implementation as an executable oracle.

---

## 3. Required Operations

A minimal conformant implementation must correctly implement the following scalar operations over the balanced ternary domain `{−1, 0, +1}`:

* `TMIN`
* `TMAX`
* `TMAJ`
* `TNOT`
* `TMUX`
* `TNET`

Vector or lane-wise behavior, where applicable, must be equivalent to applying the scalar operation independently to each lane.

---

## 4. Software Fallback Requirement

All implementations must have a correct **software fallback** path.

Hardware acceleration, if present, must:

* preserve exact semantic behavior
* be interchangeable with the software path
* not introduce observable differences in results

The absence of hardware support must not invalidate correctness.

---

## 5. Testing and Validation

Implementers are encouraged to validate correctness by:

* running the built-in tests in `examples/ternary_reference.py`
* comparing outputs against the reference implementation
* using exhaustive tests for small domains (e.g., all `3^3` inputs for `TMAJ`)

No specific test harness is mandated, but results must match reference semantics.

---

## 6. Non-Goals

Conformance does **not** require:

* optimal performance
* specific binary or ternary encodings
* SIMD, GPU, or accelerator support
* compatibility with any particular compiler or ISA

Claims beyond semantic correctness are explicitly out of scope.

---

## 7. Versioning

Conformance is defined relative to a specific released version of this repository.

Changes to `appendix.md` or `ternary_reference.py` may introduce new conformance requirements and must be versioned accordingly.

---

## 8. Statement of Intent

This conformance model exists to ensure that experimentation with ternary semantics remains **comparable, falsifiable, and interoperable**.

Correctness precedes optimization. Failure to demonstrate semantic equivalence is sufficient to invalidate a TLU implementation claim.
