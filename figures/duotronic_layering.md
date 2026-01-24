                      ┌───────────────────────────────────────────┐
                      │            APPLICATIONS / WORKLOADS        │
                      │  numeric kernels | inference | DSP-ish     │
                      │  control logic   | OS/user apps            │
                      └───────────────────────────────────────────┘
                                       │
                                       │   (opt-in use of ternary semantics)
                                       v
┌─────────────────────────────────────────────────────────────────────────────┐
│                      DUOTRONIC SEMANTIC LAYER (TERNARY)                     │
│                                                                             │
│  Meaning-carrying value space:                                              │
│    -1  = negative / false                                                   │
│     0  = neutral  / unknown                                                 │
│    +1  = positive / true                                                    │
│                                                                             │
│  Ternary-native ops (semantic kernels):                                     │
│    TMIN/TMAX   TNOT   TMAJ   TMUX   TNET                                    │
│                                                                             │
│  Software forms:                                                            │
│    intrinsics | helper ABI | packed trits | vector backends                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       │   (implemented atop / alongside binary)
                                       v
┌─────────────────────────────────────────────────────────────────────────────┐
│                     BINARY SUBSTRATE (CONTROL + TRANSPORT)                  │
│                                                                             │
│  What stays binary (non-goals to ternarize):                                │
│    - addressing, pointers, virtual memory                                   │
│    - instruction fetch/decode, control plane                                │
│    - protection, ABI, exact storage/invariants                              │
│                                                                             │
│  Provides: universality, interoperability, determinism                       │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       │
                                       v
┌─────────────────────────────────────────────────────────────────────────────┐
│                               HARDWARE (OPTIONAL)                           │
│                                                                             │
│  CPU core (binary)        +        TLU (optional coprocessor / vector unit) │
│  ────────────────                  ───────────────────────────────────────  │
│  exact control &                    ternary semantic ops at scale            │
│  orchestration                      (fallback always valid)                  │
└─────────────────────────────────────────────────────────────────────────────┘
