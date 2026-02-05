# Vast.ai Autonomous Manager

## Design Study: Autonomous GPU Compute Management

---

[![Release](https://img.shields.io/github/v/release/giorgioroth/vast-ai-autonomous-manager?include_prereleases&label=release)](https://github.com/giorgioroth/vast-ai-autonomous-manager/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

---

This repository documents a **theoretical design study** for an autonomous control loop intended to manage GPU compute resources on Vast.ai.

It is a **research artifact**, not a production system.

---

## Status

- **Type:** Design study / reference architecture
- **Implementation:** Partial, non-production, illustrative only
- **Testing:** No real-world deployment
- **Maintenance:** None guaranteed

This repository is frozen as documentation of an architectural exploration.

---

## Scope

The project explores:

- Autonomous control loops for GPU rental environments
- Hardware-first safety constraints (thermal limits, watchdogs)
- Absence-tolerant operation (systems designed to function without operator presence)
- Explicit boundary definition between control logic and execution environment

The focus is on **how such a system could be structured**, not on delivering a working product.

---

## Non-Goals

This repository does **not** provide:

- A production-ready Vast.ai manager
- A turnkey deployment solution
- Performance or profitability guarantees
- Operational support
- Benchmarks or comparative evaluations

See `NON_GOALS.md` for explicit exclusions.

---

## Implementation Notes

The code present in this repository:

- Serves as **reference scaffolding**
- Illustrates control flow and boundary decisions
- Is incomplete and not hardened
- Was developed through human-led, tool-assisted iterative design

It should be treated as **conceptual**, not executable infrastructure.

---

## Hardware References

Example hardware configurations are documented for **context only**.

They are:
- Theoretical
- Not physically built
- Not validated
- Not endorsements or recommendations

Any resemblance to real or planned systems is incidental.

---

## Relationship to ContinuumPort

This project aligns philosophically with:

- Explicit boundary definition
- Absence-tolerant system design
- Separation between specification and execution

Unlike ContinuumPort, this repository is **not** a normative specification.  
It is a design exploration.

---

## Use

This repository may be useful if you are:

- Studying autonomous system design patterns
- Exploring GPU infrastructure management concepts
- Interested in boundary-first architectural thinking

It should **not** be used directly in production environments.

---

## License

MIT License.

Use at your own risk.

---

## Author

Gh. Rotaru (Giorgio Roth)  
Independent research

---

## Final Note

This repository exists as a documented line of thinking.

It makes no claims of correctness, completeness, or fitness for purpose.
