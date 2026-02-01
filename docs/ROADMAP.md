
# Roadmap – v1.1-clean

This document describes how the project is being prepared for a clean,
public-facing release.

## Current state

The internal system exists in a production-grade form and includes:
- Autonomous pricing logic
- GPU / thermal monitoring
- UPS-aware safety checks
- Watchdog and self-recovery
- REST API and web dashboard

The internal implementation is intentionally **not fully published yet**.

## v1.1-clean goals

The goal of v1.1-clean is to publish a **minimal, readable core** that shows:
- the main control loop
- pricing decision logic
- hardware-first safety principles

without exposing:
- installer logic
- infrastructure glue
- hardware-specific automation

## Planned public structure

```

core/
vast_manager.py      # main loop (cleaned)
docs/
ARCHITECTURE.md
ROADMAP.md
README.md
LICENSE

```

## What comes next

1. Extract a clean `core/vast_manager.py`
2. Remove installer / service / API layers from public view
3. Document extension points instead of shipping full automation
4. Tag first public release as `v1.1-clean`

This repository is intentionally evolving in public.

