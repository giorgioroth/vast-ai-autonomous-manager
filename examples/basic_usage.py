#!/usr/bin/env python3
"""
Basic Usage Example - v1.1-clean

Demonstrates the minimal control loop from vast_manager.py
without production dependencies.
"""

import time
import sys
import os

# Add core to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'core'))

from vast_manager import calculate_price


def simulate_monitoring_loop():
    """
    Simulate a basic monitoring loop.
    In production, these values come from:
    - nvidia-smi (GPU stats)
    - Vast.ai API (market price)
    """
    
    print("=" * 60)
    print("VAST.AI AUTONOMOUS MANAGER - SIMULATION")
    print("=" * 60)
    
    # Mock data (replace with real sensors in production)
    market_price = 0.50  # $/GPU/hr from Vast.ai
    
    for iteration in range(5):
        # Simulate changing conditions
        utilization = 50 + (iteration * 10)  # Increasing load
        temperature = 70 + (iteration * 2)   # Heating up
        
        # Core decision logic
        new_price = calculate_price(market_price, utilization, temperature)
        
        print(f"\n[Iteration {iteration + 1}]")
        print(f"  Market: ${market_price:.2f}/hr")
        print(f"  GPU Utilization: {utilization}%")
        print(f"  GPU Temperature: {temperature}°C")
        print(f"  → Calculated Price: ${new_price:.4f}/hr")
        
        # In production: apply_price(new_price)
        # Here we just simulate
        
        time.sleep(2)  # Wait before next check
    
    print("\n" + "=" * 60)
    print("Simulation complete. See core/vast_manager.py for details.")
    print("=" * 60)


if __name__ == "__main__":
    simulate_monitoring_loop()
```
