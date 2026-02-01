
# BOUNDARIES

This document defines the explicit boundaries of the **Vast.ai Autonomous Manager**.

Its purpose is to prevent misinterpretation of the system’s role, scope, and intent.

This is a **boundary definition**, not a feature list.

---

## What this system is

This system is a **policy-bounded execution loop** for Vast.ai compute nodes.

It:

* executes predefined control logic under explicit constraints
* reacts to observable state (pricing, utilization, thermals)
* applies deterministic rules to produce actions

The system operates strictly as an **execution layer**, not as a holder of intent.

---

## What this system is not

This system is **not**:

* an autonomous agent in the cognitive or agentic sense
* a goal-optimizing system
* a long-horizon planner
* a learning or adaptive system
* a self-improving or self-modifying entity
* a system that infers, invents, or negotiates intent

The term *autonomous* refers solely to **unattended execution**,
not to authorship, agency, or decision authority.

---

## Explicit non-goals

By design, this system does **not**:

* maintain semantic, relational, or conversational memory
* carry intent across executions
* optimize objectives over time
* infer user goals or preferences
* make decisions without explicit external input
* persist internal decision state as meaning

Any notion of “strategy” exists only as **static policy**,
not as adaptive or emergent intent.

---

## Decision vs. execution

This repository intentionally separates:

* **decision inputs**
  (market data, utilization signals, thermal state)
* from **execution mechanics**
  (loops, retries, scheduling, timing)

The public code demonstrates **how execution is performed**,
not **why a decision exists**.

The decision to deploy, run, stop, or configure this system
always originates **outside** the system boundary.

---

## Relationship to intent and continuity

This system is intentionally **stateless with respect to semantic intent**.

It executes tasks.
It does not carry continuity.

Any continuity, coordination, or higher-level intent must be supplied by an
external system or by a human operator.

---

## Design intent

These boundaries are not limitations to be “fixed”.

They are **stability guarantees**.

The system is safer, more predictable, and more debuggable
because it does less —
not because it does more.

