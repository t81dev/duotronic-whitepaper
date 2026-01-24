# Appendix: Formal Semantics and Reference Material

This appendix supports the **TLU White Paper** by collecting formal definitions, truth tables, and clarifying notes that are intentionally kept out of the main document.

Sections marked **Normative** define required semantics. Other sections are informative.

---

## A. Trit Value Model (Normative)

All ternary semantics in this repository assume **balanced ternary** trits with the value set:

* **−1** : negative / false
* **0**  : neutral / unknown
* **+1** : positive / true

No other trit values are valid. Any invalid representation must normalize to one of the above values.

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

This appendix specifies *semantic meaning only*. Alternative internal encodings are permitted so long as observable behavior matches the definitions below.

---

## C. Formal Truth Tables and Definitions (Normative)

### C.0 Domain

Let the trit domain be:

```
𝕋 = { −1, 0, +1 }
```

All operators defined below act on elements of `𝕋`. For vectors or words, operators apply lane-wise unless explicitly stated otherwise.

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

#### Properties

* Commutative: `TMIN(a,b) = TMIN(b,a)` and `TMAX(a,b) = TMAX(b,a)`
* Idempotent: `TMIN(a,a) = a` and `TMAX(a,a) = a`
* Absorption:

  * `TMIN(a, TMAX(a,b)) = a`
  * `TMAX(a, TMIN(a,b)) = a`

---

### C.2 TMAJ (Ternary Majority)

#### Definition

`TMAJ(a,b,c)` returns the **median** of the multiset `{a,b,c}` under the ordering `−1 < 0 < +1`.

This definition uniquely determines all cases, including when all three inputs differ.

#### Equivalent Rule Form

* If at least two inputs are `+1`, the result is `+1`.
* Else if at least two inputs are `−1`, the result is `−1`.
* Otherwise, the result is `0`.

#### Count-Based Characterization

Let `(n−, n0, n+)` be the counts of `−1`, `0`, and `+1` among the inputs.

| (n−, n0, n+) | Example    | Result |
| -----------: | ---------- | :----: |
|      (3,0,0) | (−1,−1,−1) |   −1   |
|      (2,1,0) | (−1,−1,0)  |   −1   |
|      (2,0,1) | (−1,−1,+1) |   −1   |
|      (1,2,0) | (−1,0,0)   |    0   |
|      (1,1,1) | (−1,0,+1)  |    0   |
|      (1,0,2) | (−1,+1,+1) |   +1   |
|      (0,3,0) | (0,0,0)    |    0   |
|      (0,2,1) | (0,0,+1)   |    0   |
|      (0,1,2) | (0,+1,+1)  |   +1   |
|      (0,0,3) | (+1,+1,+1) |   +1   |

#### Properties

* Symmetric under permutation of inputs
* Idempotent: `TMAJ(a,a,b) = a`
* Median law: the result is always one of the inputs and lies between the other two

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

The numeric value is normative. Its binary or ternary integer representation is outside the scope of this definition.

#### Examples

* `(+1,+1,0,0,0,−1,0,0)` → `1`
* `(−1,−1,−1,0,+1,0,+1,0)` → `−1`
* `(0,0,0,0,0,0,0,0)` → `0`

#### Properties

* Linearity: `TNET(x ∪ y) = TNET(x) + TNET(y)` when lane-wise addition does not overflow outside `𝕋`
* Sign symmetry: `TNET(−x) = −TNET(x)` where `−x` is lane-wise negation

---

## D. Software Fallback Expectations (Normative)

All TLU operations must:

* have a correct software reference implementation
* produce identical results across scalar and vector forms
* remain semantically valid without hardware acceleration

Hardware acceleration must not alter observable behavior.

---

## E. Reference Test Vectors (Informative)

Recommended minimal tests:

* `TMIN(+1,0)=0`, `TMIN(0,−1)=−1`, `TMIN(+1,−1)=−1`
* `TMAX(−1,0)=0`, `TMAX(0,+1)=+1`, `TMAX(−1,+1)=+1`
* `TMAJ(−1,0,+1)=0` (all permutations)
* `TMAJ(+1,+1,0)=+1`, `TMAJ(−1,−1,+1)=−1`
* `TNET([+1,−1,0])=0`, `TNET([+1,+1,−1])=+1`

---

## Status

This appendix is considered **stable** once referenced by a released white paper version.
