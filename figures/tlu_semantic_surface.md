                         ┌─────────────────────────────┐
                         │            CPU (binary)      │
                         │  control | address | exact   │
                         └─────────────────────────────┘
                                      │
                                      │  (opt-in semantic ops)
                                      v
                         ┌─────────────────────────────┐
                         │             TLU             │
                         │  ternary-native semantics   │
                         │                             │
                         │   TMIN   TMAX               │
                         │   TNOT                      │
                         │   TMAJ                      │
                         │   TMUX                      │
                         │   TNET                      │
                         └─────────────────────────────┘
                                      │
                                      │  (fallback always valid)
                                      v
                         ┌─────────────────────────────┐
                         │   Software reference / ABI   │
                         │  intrinsics | helpers | tests│
                         └─────────────────────────────┘
