# The Ternary Logic Unit (TLU)

## A Duotronic Coprocessor for Meaning-Aware Computing

**Version:** 0.3 (Clarified Revision)

---

## Document Set and Authority

This paper is part of a bounded document set:

* **`TLU_WHITEPAPER.md`** — *normative* definition of TLU semantics, scope, and evaluation criteria
* **`DUOTRONIC_MODEL.md`** — *non-normative* analytic model for reasoning about semantic constraints and applicability
* Clarification documents (if present) — interpretive constraints only; no semantic authority

This paper is authoritative only with respect to TLU semantics and evaluation criteria.

---

## Abstract

Binary computing provides precision, determinism, and universality. These strengths make it the ideal substrate for control flow, addressing, and exact storage. However, many modern workloads—particularly numeric, statistical, and inference-driven systems—require explicit handling of **neutrality, uncertainty, and symmetry**. In binary systems, these properties are typically simulated using flags, sentinel values, masks, or control-flow conventions.

This paper proposes the **Ternary Logic Unit (TLU)** as a *duotronic coprocessor*: an optional, bounded execution unit that augments binary systems by making three-valued logic and balanced semantics **explicit and structurally supported**, without altering binary control planes, memory models, or ABI invariants.

In this context, *meaning-aware* refers strictly to the explicit representation and propagation of neutrality, uncertainty, and symmetry according to deterministic semantic rules.

The TLU does not replace binary computation. It is a semantic accelerator for narrowly defined classes of problems where binary representations incur unavoidable structural overhead.

---

## 1. Problem Statement

Binary logic provides two states (true/false, 1/0). This model is sufficient—and optimal—for control logic, addressing, and exact invariants. However, it poorly expresses several recurring semantic patterns:

* unknown or indeterminate values
* neutral values that should not bias computation
* symmetric positive/negative balance
* majority and reduction logic without implicit bias

In contemporary systems, these patterns are implemented indirectly through conventions such as sentinel encodings, flags, or branch-heavy logic. The resulting costs include:

* increased instruction count
* additional control-flow pressure
* representation overhead
* semantic fragility, where correctness depends on disciplined usage rather than structure

These costs are architectural in nature rather than incidental inefficiencies.

---

## 2. Historical Precedent: Floating-Point Coprocessors

Floating-point arithmetic existed in software long before hardware acceleration became common. Early implementations were slow, inconsistent, and often avoided. The introduction of IEEE-754 stabilized floating-point semantics prior to widespread hardware adoption.

Floating-point units (FPUs) succeeded because they:

* defined precise and portable semantics
* addressed an existing software burden
* remained optional and bounded
* preserved correct software fallback behavior

The TLU follows the same ordering: semantic definition first, optional hardware acceleration later.

---

## 3. Duotronic Separation Summary

The **Duotronic Model** is defined in `DUOTRONIC_MODEL.md`.
This section provides a **non-normative summary** of the separation principle for orientation only.

The duotronic approach explicitly separates responsibilities between binary and ternary domains:

| Responsibility               | Binary | Ternary |
| ---------------------------- | ------ | ------- |
| Addressing and pointers      | ✔      | ✘       |
| Control plane                | ✔      | ✘       |
| Exact storage and invariants | ✔      | ✘       |
| Semantic arithmetic          | ✘      | ✔       |
| Uncertainty propagation      | ✘      | ✔       |
| Symmetric reductions         | ✘      | ✔       |

Binary remains the universal substrate for execution and interoperability.
Ternary logic is introduced only where three-valued semantics are structurally advantageous.

---

## 4. Ternary-Native Semantics

The TLU intentionally exposes a minimal set of operations whose semantics require three-valued logic and are cumbersome to reproduce using binary primitives alone.

This paper defines **ternary logical semantics**. Balanced arithmetic is treated as a representationally compatible domain rather than a source of semantic authority.

Representative semantic kernels include:

* **TMIN / TMAX** — Kleene-style minimum and maximum with explicit neutral propagation
* **TNOT** — sign inversion that preserves neutrality
* **TMAJ** — majority vote with deterministic neutral resolution
* **TMUX** — three-way data selection controlled by a ternary condition
* **TNET** — balanced reduction defined as count(+1) minus count(−1)

These labels are mnemonic identifiers for semantic kernels, not an instruction-set commitment.

Each operation is fully defined by truth tables and deterministic propagation rules. Binary emulation is always possible but relies on multi-step sequences and control-flow conventions.

---

## 5. Software-First Validation

TLU semantics can be executed on existing binary hardware through:

* compiler intrinsics and lowering passes
* runtime helper libraries
* packed-trit and vectorized software backends

These mechanisms allow ternary semantics to be validated, tested, and measured without requiring hardware changes. Hardware acceleration, if pursued, serves only to optimize established software paths.

---

## 6. Non-Goals and Failure Cases

The TLU is not intended for:

* audio, image, or video codecs
* symbolic text processing
* general-purpose control logic
* replacing existing SIMD units, FPUs, GPUs, or CPUs

If ternary semantics do not reduce overall system complexity or cost in a given context, they should not be used. Negative results are considered valid and informative.

---

## 7. Hardware as an Optimization Layer

If implemented in hardware, a TLU may take the form of:

* a vector functional unit
* an optional coprocessor tile
* a constrained instruction-set extension

In all cases, a TLU must remain optional, bounded in scope, and semantically identical to its software reference implementation. Software fallback must remain correct and complete.

---

## 8. Evaluation Criteria

A TLU is justified only if it demonstrably provides one or more of the following under realistic workloads:

* reduced structural complexity in semantic kernels
* simpler and more robust compiler lowering
* reduced reliance on control-flow conventions
* bounded overhead that amortizes under reuse

Failure to meet these criteria invalidates the case for a TLU in that context.

---

## 9. Conclusion

The Ternary Logic Unit is a proposal to make neutrality, uncertainty, and symmetry explicit and structurally supported within modern computing systems.

It does not replace binary logic; it complements it where three-valued semantics are intrinsic to the problem domain.

Whether the TLU proves practically useful or not, clearly defining its scope and semantics establishes a principled boundary for ternary computation in contemporary systems.

---
