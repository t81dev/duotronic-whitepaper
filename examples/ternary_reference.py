#!/usr/bin/env python3
"""
ternary_reference.py

Reference (software-fallback) semantics for core TLU operations.
This module is intentionally simple, deterministic, and test-friendly.

Domain:
  𝕋 = { -1, 0, +1 }

Canonical 2-bit encoding (optional interoperability):
  00 -> -1
  01 ->  0
  10 -> +1
  11 -> invalid -> normalize to 0
"""

from __future__ import annotations

from typing import Iterable, List, Sequence


Trit = int  # must be -1, 0, +1
TritSeq = Sequence[Trit]


# -----------------------------
# Domain validation / normalize
# -----------------------------

def is_trit(x: int) -> bool:
    return x in (-1, 0, +1)


def trit(x: int) -> Trit:
    """Normalize any non-trit input to 0 (neutral)."""
    return x if is_trit(x) else 0


def normalize_trits(xs: Iterable[int]) -> List[Trit]:
    return [trit(x) for x in xs]


# -----------------------------
# Canonical 2-bit encoding helpers
# -----------------------------

def decode_bct_2bit(code: int) -> Trit:
    """
    Decode 2-bit canonical encoding:
      0b00 -> -1
      0b01 ->  0
      0b10 -> +1
      0b11 -> invalid -> normalize to 0
    """
    code &= 0b11
    if code == 0b00:
        return -1
    if code == 0b01:
        return 0
    if code == 0b10:
        return +1
    return 0


def encode_bct_2bit(x: int) -> int:
    """Encode a trit into 2-bit canonical encoding (invalid values normalize to 0)."""
    x = trit(x)
    if x == -1:
        return 0b00
    if x == 0:
        return 0b01
    return 0b10


# -----------------------------
# Core TLU operations (scalar)
# -----------------------------

def tmin(a: int, b: int) -> Trit:
    """TMIN(a,b) = min(a,b) under ordering -1 < 0 < +1."""
    a, b = trit(a), trit(b)
    return a if a <= b else b


def tmax(a: int, b: int) -> Trit:
    """TMAX(a,b) = max(a,b) under ordering -1 < 0 < +1."""
    a, b = trit(a), trit(b)
    return a if a >= b else b


def tnot(a: int) -> Trit:
    """TNOT(a) = additive inverse in balanced ternary."""
    return -trit(a)  # maps -1->+1, 0->0, +1->-1


def tmaj(a: int, b: int, c: int) -> Trit:
    """
    TMAJ(a,b,c) = median of {a,b,c} under ordering -1 < 0 < +1.
    """
    a, b, c = trit(a), trit(b), trit(c)
    s = sorted((a, b, c))
    return s[1]  # median


def tmux(cond: int, A: int, B: int, C: int) -> Trit:
    """
    TMUX(cond, A, B, C):
      cond == -1 -> A
      cond ==  0 -> B
      cond == +1 -> C
    """
    cond = trit(cond)
    A, B, C = trit(A), trit(B), trit(C)
    if cond == -1:
        return A
    if cond == 0:
        return B
    return C


def tnet(xs: Iterable[int]) -> int:
    """
    TNET(x) = sum of trits = count(+1) - count(-1).
    Output is a signed integer in [-N, +N] for N lanes.
    """
    total = 0
    for v in xs:
        total += trit(v)
    return total


# -----------------------------
# Lane-wise vector helpers
# -----------------------------

def _require_same_len(*seqs: Sequence[object]) -> int:
    """Raise ValueError if sequences differ in length; return common length."""
    if not seqs:
        raise ValueError("At least one sequence is required.")
    n = len(seqs[0])
    if any(len(s) != n for s in seqs[1:]):
        raise ValueError("All input sequences must have the same length.")
    return n


def tmin_vec(a: TritSeq, b: TritSeq) -> List[Trit]:
    _require_same_len(a, b)
    return [tmin(x, y) for x, y in zip(a, b)]


def tmax_vec(a: TritSeq, b: TritSeq) -> List[Trit]:
    _require_same_len(a, b)
    return [tmax(x, y) for x, y in zip(a, b)]


def tnot_vec(a: TritSeq) -> List[Trit]:
    return [tnot(x) for x in a]


def tmaj_vec(a: TritSeq, b: TritSeq, c: TritSeq) -> List[Trit]:
    _require_same_len(a, b, c)
    return [tmaj(x, y, z) for x, y, z in zip(a, b, c)]


def tmux_vec(cond: TritSeq, A: TritSeq, B: TritSeq, C: TritSeq) -> List[Trit]:
    _require_same_len(cond, A, B, C)
    return [tmux(k, a, b, c) for k, a, b, c in zip(cond, A, B, C)]


# -----------------------------
# Minimal conformance checks
# -----------------------------

def _assert_eq(got, exp, msg: str = "") -> None:
    if got != exp:
        raise AssertionError(f"{msg}\n  got: {got}\n  exp: {exp}")


def run_minimal_tests() -> None:
    # TMIN / TMAX (reference vectors)
    _assert_eq(tmin(+1, 0), 0, "TMIN(+1,0)")
    _assert_eq(tmin(0, -1), -1, "TMIN(0,-1)")
    _assert_eq(tmin(+1, -1), -1, "TMIN(+1,-1)")

    _assert_eq(tmax(-1, 0), 0, "TMAX(-1,0)")
    _assert_eq(tmax(0, +1), +1, "TMAX(0,+1)")
    _assert_eq(tmax(-1, +1), +1, "TMAX(-1,+1)")

    # TMAJ (all permutations of -1,0,+1 -> 0)
    perms = [(-1, 0, +1), (-1, +1, 0), (0, -1, +1), (0, +1, -1), (+1, -1, 0), (+1, 0, -1)]
    for p in perms:
        _assert_eq(tmaj(*p), 0, f"TMAJ{p}")

    _assert_eq(tmaj(+1, +1, 0), +1, "TMAJ(+1,+1,0)")
    _assert_eq(tmaj(-1, -1, +1), -1, "TMAJ(-1,-1,+1)")

    # TNET
    _assert_eq(tnet([+1, -1, 0]), 0, "TNET([+1,-1,0])")
    _assert_eq(tnet([+1, +1, -1]), +1, "TNET([+1,+1,-1])")

    # TNOT
    _assert_eq(tnot(-1), +1, "TNOT(-1)")
    _assert_eq(tnot(0), 0, "TNOT(0)")
    _assert_eq(tnot(+1), -1, "TNOT(+1)")

    # TMUX
    _assert_eq(tmux(-1, -1, 0, +1), -1, "TMUX(-1, A,B,C)")
    _assert_eq(tmux(0, -1, 0, +1), 0, "TMUX(0, A,B,C)")
    _assert_eq(tmux(+1, -1, 0, +1), +1, "TMUX(+1, A,B,C)")

    # Canonical encoding normalization
    _assert_eq(decode_bct_2bit(0b11), 0, "decode invalid -> 0")
    _assert_eq(encode_bct_2bit(123), 0b01, "encode invalid -> 0")

    # Algebraic sanity (informative properties)
    dom = (-1, 0, +1)
    for a in dom:
        for b in dom:
            _assert_eq(tmin(a, b), tmin(b, a), f"TMIN commutes ({a},{b})")
            _assert_eq(tmax(a, b), tmax(b, a), f"TMAX commutes ({a},{b})")
            _assert_eq(tmin(a, a), a, f"TMIN idempotent ({a})")
            _assert_eq(tmax(a, a), a, f"TMAX idempotent ({a})")
            _assert_eq(tmin(a, tmax(a, b)), a, f"TMIN absorption ({a},{b})")
            _assert_eq(tmax(a, tmin(a, b)), a, f"TMAX absorption ({a},{b})")

        _assert_eq(tnot(tnot(a)), a, f"TNOT involution ({a})")

    print("OK: minimal reference tests passed.")


def run_exhaustive_tests() -> None:
    """Optional exhaustive checks: TMAJ (3^3) and TMUX (3*3^3)."""
    dom = (-1, 0, +1)

    # Exhaustive TMAJ: 27 cases
    for a in dom:
        for b in dom:
            for c in dom:
                s = sorted((a, b, c))
                _assert_eq(tmaj(a, b, c), s[1], f"TMAJ median ({a},{b},{c})")

    # Exhaustive TMUX: 81 cases
    for cond in dom:
        for A in dom:
            for B in dom:
                for C in dom:
                    exp = A if cond == -1 else (B if cond == 0 else C)
                    _assert_eq(tmux(cond, A, B, C), exp, f"TMUX ({cond},{A},{B},{C})")

    print("OK: exhaustive reference tests passed.")


if __name__ == "__main__":
    run_minimal_tests()

    # Enable heavier checks via: TLU_EXHAUSTIVE=1 python ternary_reference.py
    import os
    if os.getenv("TLU_EXHAUSTIVE") == "1":
        run_exhaustive_tests()
