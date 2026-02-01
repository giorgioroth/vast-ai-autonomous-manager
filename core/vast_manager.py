"""
vast_manager.py — v1.1-clean (public core)

This file contains the minimal autonomous control loop used by the
Vast.ai Autonomous Manager.

Included:
- main loop structure
- pricing decision logic (simplified)
- hardware-first safety placeholders

Excluded (by design):
- systemd integration
- REST API
- email / alerts
- UPS automation
- installer logic

This is a public, educational core.
"""

import time


def calculate_price(market_price: float, utilization: float, temperature: float) -> float:
    """
    Simplified pricing logic.

    This function represents the *decision core* of the system.
    The real implementation is more complex and hardware-aware.
    """
    price = market_price

    if utilization < 30:
        price *= 0.9

    if temperature > 80:
        price *= 1.1

    return round(price, 4)


def main_loop():
    """
    Minimal autonomous loop.
    """
    market_price = 0.50  # placeholder
    utilization = 50     # placeholder
    temperature = 70     # placeholder

    while True:
        new_price = calculate_price(market_price, utilization, temperature)
        print(f"[v1.1-clean] Calculated price: ${new_price}/GPU/hr")

        time.sleep(10)


if __name__ == "__main__":
    main_loop()
