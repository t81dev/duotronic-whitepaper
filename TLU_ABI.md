# TLU_ABI.md — Ternary Logic Unit ABI

**Status:** Normative (ABI Contract)
**Version:** 0.1

This document defines a stable Application Binary Interface (ABI) for invoking
**Ternary Logic Unit (TLU)** semantics from software, toolchains, and optional
accelerator backends.

This ABI is **CPU-agnostic**. It is intended to be implementable on any platform
(x86-64, AArch64, RISC-V, etc.) as a pure software library, and optionally
accelerated via platform-specific mechanisms.

This ABI does not define instruction encodings, hardware interfaces, or performance
characteristics.

If any inconsistency exists between this document and `appendix.md`, `appendix.md`
is authoritative for operator semantics. This document is authoritative for calling
conventions, type layout, and boundary normalization.

---

## 1. Design Goals

The ABI is designed to:

* provide a **portable** invocation surface for TLU semantics
* permit **software-first** conformance on all platforms
* enable compilers to lower intrinsics to a stable C ABI
* allow optional backends (SIMD, accelerators, coprocessors) without changing the API
* remain minimal and easy to bind from multiple languages

---

## 2. Value Model and Normalization

### 2.1 Canonical Trit Values

All trit arguments and returns use balanced ternary values:

* `-1` negative / false
* `0`  neutral / unknown
* `+1` positive / true

No other values are valid at the semantic level.

### 2.2 Boundary Normalization

All ABI entry points must normalize input trits to the canonical domain prior to
evaluation:

* any value `< 0` normalizes to `-1`
* `0` normalizes to `0`
* any value `> 0` normalizes to `+1`

This rule ensures language and platform interoperability.

**Note:** If a consuming context requires strict rejection of invalid inputs,
that policy is out of scope for this ABI and must be enforced by the caller.

---

## 3. Types

### 3.1 `tlu_trit_t`

The canonical ABI trit type is a signed 8-bit integer.

```c
typedef int8_t tlu_trit_t;
```

The value domain at the API boundary is `{-1, 0, +1}` after normalization.

### 3.2 `tlu_i32_t`

For numeric results of reductions, the canonical ABI integer type is 32-bit signed.

```c
typedef int32_t tlu_i32_t;
```

`TNET` returns a numeric value in `[-N, +N]` (per `appendix.md`), represented as
`tlu_i32_t`. Saturation, clipping, or modular reduction is not permitted within
the definition of `TNET`.

---

## 4. Scalar Operations

All scalar functions must implement semantics observationally equivalent to the
definitions in `appendix.md`.

### 4.1 `tlu_tmin`

```c
tlu_trit_t tlu_tmin(tlu_trit_t a, tlu_trit_t b);
```

Returns `TMIN(a,b)`.

### 4.2 `tlu_tmax`

```c
tlu_trit_t tlu_tmax(tlu_trit_t a, tlu_trit_t b);
```

Returns `TMAX(a,b)`.

### 4.3 `tlu_tmaj`

```c
tlu_trit_t tlu_tmaj(tlu_trit_t a, tlu_trit_t b, tlu_trit_t c);
```

Returns `TMAJ(a,b,c)`.

### 4.4 `tlu_tnot`

```c
tlu_trit_t tlu_tnot(tlu_trit_t a);
```

Returns `TNOT(a)`.

### 4.5 `tlu_tmux`

```c
tlu_trit_t tlu_tmux(tlu_trit_t cond, tlu_trit_t A, tlu_trit_t B, tlu_trit_t C);
```

Returns `TMUX(cond, A, B, C)`.

---

## 5. Reduction Operation

### 5.1 `tlu_tnet`

```c
tlu_i32_t tlu_tnet(const tlu_trit_t* x, size_t n);
```

Returns `TNET(x)` where `x` is a vector of length `n` in the trit domain.

* The function must treat each element lane-wise.
* Inputs must be normalized per §2.2 prior to aggregation.
* The numeric value returned must equal `count(+1) - count(-1)`.

If `x == NULL` and `n > 0`, behavior is undefined. Callers must provide valid
pointers.

---

## 6. Vector (Lane-wise) Optional Extensions

This ABI permits, but does not require, optional vector entry points.

If provided, vector entry points must be observationally equivalent to applying
the scalar operator lane-wise.

Suggested naming convention (optional):

* `tlu_tmin_n(tlu_trit_t* out, const tlu_trit_t* a, const tlu_trit_t* b, size_t n)`
* `tlu_tmax_n(...)`, `tlu_tmaj_n(...)`, etc.

Vector entry points must not alter semantics.

---

## 7. Conformance and Testing

An implementation conforms to this ABI if:

* all functions specified here exist with the stated signatures and type layouts
* boundary normalization rules are followed
* results are observationally equivalent to the normative semantics in `appendix.md`

The reference oracle in `examples/ternary_reference.py` may be used to validate
behavior. Conformance requirements are defined in `CONFORMANCE.md`.

---

## 8. Versioning and Compatibility

The ABI version applies to:

* function names and signatures
* type layouts
* normalization rules

Changes that break binary compatibility require a major version increment.

Implementations must state:

* the ABI version implemented
* the repository version against which conformance is claimed

---

## 9. Non-Goals

This ABI does not define:

* instruction encodings or ISA extensions
* hardware register models
* memory layouts beyond pointer/length conventions
* concurrency semantics or thread-safety guarantees
* error-reporting mechanisms for invalid inputs

Such concerns are delegated to consuming environments.

---

## 10. Header Recommendation (Informative)

Implementations are encouraged to provide a single public header, e.g. `tlu_abi.h`,
containing the type definitions and function prototypes in this document.

---
