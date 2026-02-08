# Duotronic TLU White Paper

This repository hosts a **systems white paper** defining the concept, scope, and evaluation criteria for a **Ternary Logic Unit (TLU)** operating in a **duotronic** (binary + ternary) computing model.

The purpose of this repo is *foundational*, not experimental. It defines semantics, boundaries, and falsifiable claims that downstream implementations may reference or reject.

## What this repository is

* A stable, implementation-agnostic description of a **TLU as a coprocessor**
* A precise statement of **ternary-native semantics** that cannot be reduced cleanly to binary
* A boundary-setting document describing **where ternary should and should not apply**
* A reference point for compilers, runtimes, and system experiments

## What this repository is not

* Not a hardware design
* Not a chip proposal or fabrication plan
* Not a performance marketing document
* Not a claim that ternary replaces binary

Binary remains the control and transport substrate. Ternary augments it where meaning, neutrality, and symmetry are first-class concerns.

## Audience

This document is written for:

* compiler engineers
* systems researchers
* hardware architects
* numerical computing practitioners

It assumes familiarity with ISAs, coprocessors, and software/hardware co-design.

## Contents

* **TLU_WHITEPAPER.md** — the main white paper
* **figures/** — diagrams and illustrations (optional)
* **appendix/** — truth tables, formal definitions, and extended notes (optional)

## Relationship to other projects

This repository is intentionally upstream of any implementation. Related projects may include:

* Compiler lowering and runtimes (e.g., GCC plugins)
* System-level experiments (e.g., paging or memory representation)
* Numeric libraries using balanced ternary representations

Those projects may reference this white paper, but this paper does not depend on their success.

## Status

**Drafting (semantic freeze target before optimization work)**

The goal is clarity and falsifiability, not momentum.

## Document Structure and Reading Order

This repository is intentionally structured to separate semantics, analysis, and interpretation:

1. **TLU_WHITEPAPER.md**  
   Normative definition of TLU semantics, scope, and evaluation criteria.

2. **DUOTRONIC_MODEL.md**  
   Non-normative analytic model describing semantic constraint surfaces and applicability.

3. **DUOTRONIC_MODEL_CLARIFICATIONS.md**  
   Interpretive constraints that explicitly invalidate common misreadings.

4. **TERMINOLOGY_ALIGNMENT.md**
   Canonical term mapping and conflict-resolution notes aligned with ecosystem glossary guidance.

Readers are strongly advised to consult the clarification document before drawing conclusions or proposing extensions.

## License

MIT

This repository is frozen at v0.3 except for errata. Experimental work lives elsewhere.
