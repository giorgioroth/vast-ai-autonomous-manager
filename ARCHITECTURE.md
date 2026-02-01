# Architecture Overview

This project is designed as a self-healing autonomous control loop for Vast.ai compute nodes.

Core components:
- vast_manager.py – pricing + monitoring loop
- systemd services – lifecycle & watchdog
- REST API – remote control & automation
- Web dashboard – read-only observability

Design principles:
- No interactive dependencies at runtime
- Safe defaults
- Fail-fast + self-recover
- Hardware-first thinking (GPU, UPS, thermals)
