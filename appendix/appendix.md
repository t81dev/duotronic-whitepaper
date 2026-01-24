# Appendix: Formal Semantics and Reference Material

This appendix supports the **TLU White Paper** by collecting formal definitions, truth tables, and clarifying notes that are intentionally kept out of the main document.

The appendix is normative where explicitly stated and informative elsewhere.

---

## A. Trit Value Model (Normative)

All ternary semantics in this repository assume **balanced ternary** trits with the value set:

* **−1** : negative / false
* **0**  : neutral / unknown
* **+1** : positive / true

No other trit values are valid. Invalid encodings must normalize to one of the above.

---

## B. Canonical Trit Encoding (Normative)

A canonical binary encoding is assumed for software and hardware interoperability:

| Binary bits | Trit value               |
| ----------- | ------------------------ |
| `00`        | −1                       |
| `01`        | 0                        |
| `10`        | +1                       |
| `11`        | invalid (must normalize) |

Normalization (`TNORMALIZE`) clamps invalid encodings to `0`.

---

## C. Truth Tables (Normative)

### C.1 TNOT (Ternary NOT)

| input | output |
| ----- | ------ |
| −1    | +1     |
| 0     | 0      |
| +1    | −1     |

---

### C.2 TMIN / TMAX (Kleene Logic)

Ordering: −1 < 0 < +1

**TMIN(a,b)** returns the lesser value, propagating `0` when applicable.

**TMAX(a,b)** returns the greater value, propagating `0` when applicable.

---

### C.3 TMAJ (Ternary Majority)

| Inputs (a,b,c) | Result |
| -------------- | ------ |
| two or more +1 | +1     |
| two or more 0  | 0      |
| two or more −1 | −1     |
| (−1,0,+1)      | 0      |

---

### C.4 TMUX (Three-Way Select)

TMUX(cond, A, B, C):

| cond | result |
| ---- | ------ |
| −1   | A      |
| 0    | B      |
| +1   | C      |

---

### C.5 TNET (Balanced Reduction)

TNET computes:

```
count(+1) − count(−1)
```

Zeros do not contribute. The operation is carry-free and symmetric.

---

## D. Software Fallback Expectations (Informative)

All TLU operations must:

* have a correct software reference implementation
* produce bit-for-bit identical results to any hardware implementation
* remain valid under vectorized and scalar execution

Hardware acceleration must not change semantics.

---

## E. Non-Normative Notes

* This appendix intentionally avoids hardware timing, pipeline, or encoding details.
* Future revisions may add algebraic identities or formal proofs if required.

---

## Status

Appendix content is considered **stable** once referenced by a released white paper version.
