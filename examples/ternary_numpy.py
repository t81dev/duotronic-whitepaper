"""
ternary_numpy.py

NON-NORMATIVE, EXPERIMENTAL HELPERS.

This file provides NumPy-based convenience wrappers around the
reference TLU semantics defined in `ternary_reference.py`.

It is intended for experimentation, prototyping, and exploration only.
It must not be used as a semantic reference or treated as authoritative.
"""

from __future__ import annotations
import numpy as np
from ternary_reference import tmin, tmax, tnot, tmaj, tmux, tnet

# Vectorized wrappers (correctness-first; not necessarily fast)
vtmin = np.vectorize(tmin)
vtmax = np.vectorize(tmax)
vtnot = np.vectorize(tnot)
vtmaj = np.vectorize(tmaj)
vtmux = np.vectorize(tmux)

def vtnet(x: np.ndarray) -> int:
    # preserve reference semantics via Python int sum
    return int(np.sum(np.vectorize(lambda z: z if z in (-1,0,1) else 0)(x)))
