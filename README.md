# vast-ai-autonomous-manager

---

[![Release](https://img.shields.io/github/v/release/giorgioroth/vast-ai-autonomous-manager?include_prereleases&label=release)](https://github.com/giorgioroth/vast-ai-autonomous-manager/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Autonomous node manager for Vast.ai - Dynamic pricing, GPU monitoring, auto-bidding &amp; watchdog for dual RTX 5090 compute rigs. Production-ready with REST API, web dashboard, and systemd integration.

---

## Why this exists

This project exists because production AI infrastructure is often discussed at a theoretical level, while the real complexity lives in the *control loops* that keep machines safe, profitable, and autonomous over long periods of time.

Before dashboards, APIs, and automation layers, there is always a core decision loop: observe → decide → act → wait.
This repository exposes that core logic in a minimal, readable form, intentionally separated from installers, credentials, and hardware-specific glue.

The original system behind this project ran in a real production environment.
What is published here is not the full machinery, but the *thinking model* behind it — a hardware-first approach where safety, thermals, and stability are treated as first-class constraints, not afterthoughts.

This repository evolves in public by design.
It is meant to be read, understood, and adapted — not deployed as-is.

---

For explicit design boundaries and deliberate non-goals, see:
- [`BOUNDARIES.md`](./BOUNDARIES.md)
- [`NON_GOALS.md`](./NON_GOALS.md)

