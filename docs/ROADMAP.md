
## Roadmap — v1.1-clean

This document describes how the project is prepared for a clean, public-facing release.

This roadmap must be read in conjunction with:

* `BOUNDARIES.md`
* `NON_GOALS.md`

It defines what is published, not what is promised.

---

## Current state

The internal system exists in a production-grade form and includes:

* autonomous pricing logic
* GPU and thermal monitoring
* UPS-aware safety checks
* watchdog and self-recovery mechanisms
* REST API and web dashboard

The internal implementation is intentionally **not** fully published.

What is made public is the **core execution model**, not the complete operational stack.

---

## v1.1-clean goals

The goal of v1.1-clean is to publish a minimal, readable, boundary-defined core that demonstrates:

* the main control loop (observe → decide → act → wait)
* pricing decision logic
* hardware-first safety principles

**without exposing:**

* installer logic
* service management
* credentials or secrets
* infrastructure glue
* hardware-specific automation

This release focuses on **clarity and inspectability**, not deployability.

---

## Planned public structure

```
core/
  vast_manager.py      # cleaned main execution loop

docs/
  ARCHITECTURE.md
  ROADMAP.md
  BOUNDARIES.md
  NON_GOALS.md
  HARDWARE_REFERENCE.md

README.md
LICENSE
```

---

## What comes next

The following steps define the completion of v1.1-clean:

* extract a clean core (`core/vast_manager.py`)
* remove installer, service, and API layers from public view
* document extension points instead of shipping full automation
* tag the first public release as `v1.1-clean`
* mark the release as **pre-release** to signal non-deployable intent

No functional expansion is planned as part of this phase.

---

## Post-release note

v1.1-clean is considered a **stable public baseline**.

Any future changes, **should they arise**, will prioritize:

* boundary clarity
* documentation
* explicit non-goals

over feature growth, agentic behavior, or increased autonomy.

This repository evolves in public by design, but remains constrained by its stated boundaries.
