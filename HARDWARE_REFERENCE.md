## HARDWARE REFERENCE

## Dual RTX 5090 Workstation — Silent, Stable, Long-Run (2025)

This document describes a **reference hardware configuration** developed over two months of real-world iteration.

It is **not a requirement** to run `vast-ai-autonomous-manager`.  
It is a **hardware baseline** for users who prioritize thermal stability, acoustic comfort, and long-running AI workloads over peak benchmarks or aesthetics.

---

## Design principles

This build is guided by the following principles:

- **Thermal stability > peak performance**
- **Acoustic comfort > maximum airflow**
- **Predictability > aggressive tuning**
- **Separation of compute, storage, and data plane**
- **Low maintenance over custom complexity**

No component was selected for RGB, novelty, or short-lived benchmarks.

---

## Chassis & airflow

### Case
- **be quiet! Dark Base Pro 901 (Black)**  
  High-airflow full tower with excellent acoustic dampening  
  Supports extreme fan density without turbulence

### Dust management
- **2× GELID SOLUTIONS Magnetic Mesh 140 mm**  
  Washable, low-restriction filters with magnetic mounting  
  Additional GAUDER magnetic strips for secure sealing

### Airflow capacity
Up to **17 fans total**, allowing very low PWM curves while maintaining headroom.

---

## Power delivery

### Power Supply
- **Seasonic Prime PX-2200 ATX 3.1 — 2200 W**  
  Fully modular, <20 dBA operation, 12-year warranty  
  Safe headroom for dual RTX 5090 under sustained load  
  Eco Mode enabled for low idle consumption

---

## GPUs

### Graphics cards
- **2× ASUS ROG Astral LC GeForce RTX 5090 — 32 GB GDDR7**  
  Each GPU cooled by a dedicated 360 mm AIO  
  Controlled via ASUS GPU Tweak III

### GPU support
- **2× ASUS ROG Herculx GPU brackets**  
  Horizontal mounting, zero sag, no airflow obstruction

---

## CPU & cooling

### Processor
- **AMD Ryzen 9 9950X3D**  
  16 cores / 32 threads  
  144 MB cache  
  Boost up to 5.7 GHz

### CPU cooling
- **be quiet! Silent Loop 3 — 420 mm AIO**  
  3× Silent Wings 4 140 mm PWM

### Thermal interface
- **Thermal Grizzly Duronaut** thermal paste  
- **Thermal Grizzly AM5 Contact & Sealing Frame**

---

## Motherboard

- **ASUS ROG Crosshair X870E Extreme (E-ATX)**  
  20+2+2 power stages  
  3× PCIe 5.0  
  Wi-Fi 7  
  Integrated diagnostics and LCD

---

## Memory

- **256 GB DDR5 (2×128 GB) Crucial Pro 5600 MT/s CL46**  
  AMD EXPO compatible  
  Selected for stability and capacity over latency

---

## Storage (local)

### Primary storage
- **2× Samsung 9100 PRO 8 TB PCIe 5.0**  
  Configured as **RAID 1** → 8 TB usable  
  Focus on reliability over raw throughput

### Optional scratch
- Additional 4 TB SSDs on secondary M.2 slots for AI scratch space

---

## Cooling & fans (total: 17)

- 3× preinstalled case fans
- 3× CPU AIO fans (420 mm)
- 6× GPU AIO fans (2×360 mm)
- 8× additional Silent Wings 4 140 mm PWM (high-speed)

### Recommended airflow layout (simplified)

- **Front (Intake):** CPU radiator 420 mm push/pull
- **GPU radiators:** Dedicated airflow paths per GPU
- **Top (Exhaust):** 3×140 mm
- **Bottom (Intake):** 2×140 mm (filtered)
- **Rear (Exhaust):** 1×140 mm

---

## Expected operating characteristics (AI load)

- **Dual RTX 5090:** 65–70 °C
- **Ryzen 9950X3D:** ~60 °C
- **Target noise level:** <35 dBA  
  (Quiet PWM profiles, no aggressive fan ramps)

---

## External storage & data plane

### NAS
- **Synology DS923+**
  - 4 bays
  - 48 TB raw (4×12 TB)
  - SHR-2 → ~24 TB usable
  - 32 GB ECC RAM
  - 2 TB NVMe cache
  - 10 GbE expansion

### Networking
- **10 GbE internal network**
  - Zyxel AX7501-B0 (ONT + router, 10 GbE port)
  - Intel X550-T2 dual-port NIC (PC)
  - UGREEN Cat8 cabling

This separates **compute I/O** from **bulk data and backups**.

---

## Power protection

- **APC Smart-UPS SMT3000IC**
  - 3000 VA
  - SmartConnect monitoring
  - Clean shutdown support

---

## Auxiliary components

- **ARCTIC PWM Fan Hub (10 ports, SATA powered)**
- **25× QitinDasen ferrite cores (RFI/EMI suppression)**

---

## Summary

This configuration delivers:

- Dual RTX 5090 compute
- High-capacity, stable memory
- Redundant local storage
- Dedicated NAS + 10 GbE data plane
- Quiet operation under sustained load
- UPS-backed power integrity

It is designed to **run continuously**, not to impress briefly.

---

## Scope note

This hardware reference is provided **as-is**, without obligation or endorsement.

`vast-ai-autonomous-manager` does **not** depend on this configuration.  
The system is hardware-agnostic by design.

This document exists to share **practical engineering decisions**, not requirements.

It describes a theoretically sound, hardware-first configuration,
derived from careful design and component-level reasoning,
not from empirical benchmarking or performance claims.

