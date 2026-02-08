# Terminology Alignment Notes

Roadmap linkage:
- `t81-roadmap#1`
- `t81-roadmap/PHASE0_ALIGNMENT_MATRIX.md` (`P0-A1`)

Snapshot date: 2026-02-08.

This note aligns whitepaper terminology with current ecosystem glossary and runtime/spec language.

## Canonical Mapping

| Whitepaper Term | Canonical Ecosystem Term | Source Alignment |
| --- | --- | --- |
| `TLU` | `Ternary Logic Unit` | Primary whitepaper concept; treated as a coprocessor concept, not standalone system replacement. |
| `Duotronic` | `Binary + ternary co-computing model` | Consistent with `t81-docs` interpretive wording and `t81-foundation` architecture constraints. |
| `Normative` (whitepaper context) | `Formal semantics source` | Must remain aligned with `t81-foundation/spec` for executable semantics disputes. |
| `Interpretive` | `Contextual/explanatory guidance` | Aligns with `t81-docs` formal-vs-interpretive boundary rules. |

## Conflicts and Resolutions

1. Potential conflict:
   interpreting `duotronic` as a replacement for binary substrate.
   Resolution:
   this repository explicitly keeps binary as control/transport substrate and positions ternary as augmentation.
2. Potential conflict:
   treating whitepaper claims as runtime contract.
   Resolution:
   executable contract authority remains with runtime repos (for example `t81-vm` contract artifacts), while this repo stays conceptual/normative at proposal layer.

## Maintenance Rule

When adding or redefining terms in `README.md` or `TLU_WHITEPAPER.md`, update this file and link any cross-repo terminology impacts in `t81-roadmap`.
