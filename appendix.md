# Appendix: Formal Semantics and Reference Material

This appendix supports the **TLU White Paper** by collecting formal definitions,
truth tables, and clarifying notes that are intentionally kept out of the main document.

Sections marked **Normative** define required semantics.
Other sections are informative and non-binding.

The executable reference implementation in `examples/ternary_reference.py`
is required to be **observationally equivalent** to all normative definitions herein.

---

## A. Trit Value Model (Normative)

All ternary semantics in this repository assume **balanced ternary** trits with the value set:

* **−1** : negative / false
* **0**  : neutral / unknown
* **+1** : positive / true

No other trit values are valid. Any invalid representation must normalize
to one of the above values.

The total order over trits is:

```
−1 < 0 < +1
```

---

## B. Canonical Trit Encoding (Normative)

For software and interoperability purposes, a canonical binary encoding is assumed:

| Binary bits | Trit value |
| ----------- | ---------- |
| `00`        | −1         |
| `01`        | 0          |
| `10`        | +1         |
| `11`        | invalid    |

Invalid encodings **must normalize to `0`**.

Normalization must occur **prior to semantic evaluation** of any operator.

This appendix specifies *semantic meaning only*.
Alternative internal encodings are permitted so long as **observable behavior**
matches the definitions below.

---

## C. Formal Truth Tables and Definitions (Normative)

### C.0 Domain and Vector Semantics

Let the trit domain be:

```
𝕋 = { −1, 0, +1 }
```

All scalar operators act on elements of `𝕋`.

For vectors or words, operators apply **lane-wise**
unless explicitly stated otherwise.

Reduction operators specify their aggregation semantics
independently of storage or representation.

**Observable behavior** refers solely to the returned trit or numeric value
defined by the operator semantics, excluding timing, side effects,
memory access patterns, or resource usage.

---

### C.1 TMIN and TMAX (Kleene Min/Max)

#### Definition

`TMIN(a,b)` returns the minimum of `a` and `b` under the ordering `−1 < 0 < +1`.

`TMAX(a,b)` returns the maximum of `a` and `b` under the same ordering.

These definitions treat `0` as a first-class middle value and require no special-case handling.

#### Truth Tables

**TMIN(a,b)**

|  a \ b |  −1 |  0  |  +1 |
| -----: | :-: | :-: | :-: |
| **−1** |  −1 |  −1 |  −1 |
|  **0** |  −1 |  0  |  0  |
| **+1** |  −1 |  0  |  +1 |

**TMAX(a,b)**

|  a \ b |  −1 |  0  |  +1 |
| -----: | :-: | :-: | :-: |
| **−1** |  −1 |  0  |  +1 |
|  **0** |  0  |  0  |  +1 |
| **+1** |  +1 |  +1 |  +1 |

#### Properties (Informative)

* Commutative
* Associative
* Idempotent
* Absorption laws hold
* Monotonic with respect to trit ordering

---

### C.2 TMAJ (Ternary Majority)

#### Definition

`TMAJ(a,b,c)` returns the **median** of the multiset `{a,b,c}` under the ordering `−1 < 0 < +1`.

This definition uniquely determines all cases, including when all three inputs differ.

#### Equivalent Rule Form

* If at least two inputs are `+1`, the result is `+1`
* Else if at least two inputs are `−1`, the result is `−1`
* Otherwise, the result is `0`

#### Properties (Informative)

* Symmetric under permutation
* Idempotent
* Median law holds
* Stability under replacement

---

### C.3 TNET (Balanced Reduction)

#### Definition

For a vector of trits `x ∈ 𝕋^N`:

```
TNET(x) = Σ xᵢ = count(+1) − count(−1)
```

Zeros contribute no value.

#### Output Range

```
TNET(x) ∈ [ −N , +N ]
```

The numeric value is normative.

**Saturation, clipping, or modular reduction of the numeric result is not permitted**
within the definition of `TNET` itself.

The representation of the result is explicitly out of scope.

---

### C.4 TNOT (Unary Negation)

#### Definition

`TNOT(a)` returns the additive inverse of `a` in balanced ternary.

#### Truth Table

|  a  | TNOT(a) |
| :-: | :-----: |
|  −1 |    +1   |
|  0  |    0    |
|  +1 |    −1   |

---

### C.5 TMUX (Ternary Select)

#### Definition

`TMUX(cond, A, B, C)` selects one of three values based on a ternary condition:

| cond | result |
| :--: | :----: |
|  −1  |    A   |
|   0  |    B   |
|  +1  |    C   |

Selection is deterministic and side-effect free.

---

## D. Software Fallback Expectations (Normative)

All TLU operations must:

* have a correct software reference implementation
* produce identical results across scalar and vector forms
* remain semantically valid without hardware acceleration

Hardware acceleration must not alter observable behavior.

---

## E. Reference Test Vectors (Informative)

Representative tests include:

* `TMIN(+1,0)=0`, `TMIN(0,−1)=−1`
* `TMAX(−1,0)=0`, `TMAX(0,+1)=+1`
* `TMAJ(−1,0,+1)=0`
* `TNET([+1,+1,−1])=+1`
* `TNOT(−1)=+1`
* `TMUX(0,A,B,C)=B`

---

## F. Informative Context and Analogues (Informative)

Related semantic patterns appear in:

* three-valued logic in databases (e.g., SQL `NULL`)
* median filters in signal processing
* majority voting in fault-tolerant systems

These analogues are provided for orientation only.

---

## G. Worked Semantic Examples (Informative)

This section provides small examples illustrating **structural friction**
when certain semantic patterns are encoded in binary systems.

These examples imply no performance claim or architectural recommendation.

---

### G.1 Neutrality Without Sentinel Conventions

**TLU expression**

```
y = TMIN(x, 0)
```

Neutrality propagates structurally.

**Binary encoding**

Requires sentinels, flags, or control-flow discipline.

**Observation**

TLU encodes neutrality as data.
Binary systems encode neutrality by convention.

---

### G.2 Majority Without Bias

**TLU expression**

```
r = TMAJ(a, b, c)
```

Median rule applies uniformly.

**Binary encoding**

Requires explicit case analysis and tie-breaking logic.

**Observation**

TLU encodes majority directly.
Binary systems reconstruct it procedurally.

---

### G.3 Balanced Reduction

**TLU expression**

```
s = TNET(x)
```

Positive and negative contributions cancel symmetrically.

**Binary encoding**

Requires multiple counters or post-processing.

**Observation**

TLU encodes balance structurally.
Binary systems approximate balance arithmetically.

---

## Status

This appendix is considered **stable** once referenced by a released white paper version.

---
