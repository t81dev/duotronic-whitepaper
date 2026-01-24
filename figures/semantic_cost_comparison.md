                 SAME INTENT: "3-valued meaning" (−1 / 0 / +1)

┌──────────────────────────────────────┐        ┌─────────────────────────────┐
│  Binary simulation (today)           │        │  Ternary-native (TLU/ABI)    │
├──────────────────────────────────────┤        ├─────────────────────────────┤
│  Represent unknown/neutral via:      │        │  Unknown/neutral is a value  │
│   - flags / masks                    │        │   (0 is first-class)         │
│   - NaN-like conventions             │        │                             │
│   - sentinel encodings               │        │  Semantics encoded directly: │
│                                      │        │   - truth tables             │
│  Implement ternary logic via:        │        │   - deterministic propagation│
│   - multi-step bit tricks            │        │                             │
│   - branchy control flow             │        │  Implement via:              │
│   - extra compares                   │        │   - single semantic op        │
│                                      │        │   - vector lanes / packed trits│
│  Costs appear as:                    │        │                             │
│   - instruction count                │        │  Costs appear as:            │
│   - branch pressure                  │        │   - bounded decode/pack cost  │
│   - semantic fragility               │        │   - reduced convention overhead│
└──────────────────────────────────────┘        └─────────────────────────────┘
