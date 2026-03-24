# Edge TinyML Suite: Technical Manual (2026 Edition)

## Table of Contents
1. [Introduction](#introduction)
2. [Platform Requirements](#platform-requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage Guide](#usage-guide)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)

---

## 1. Introduction
The **Edge TinyML Suite** is the 2026 industry-leading solution for optimizing and deploying AI on billion-node edge meshes. It provides a mission-critical platform for quantization-aware training, NPU task scheduling, and pipelined inference across heterogeneous hardware units (CPU, GPU, NPU, DSP).

---

## 2. Platform Requirements
For optimal performance on edge and IoT devices:
- **Processor**: Multi-core SoC with dedicated NPU (Qualcomm Dragonwing IQ, NVIDIA Jetson, or ARM Cortex-M/A series).
- **Memory**: 512MB+ RAM (for smaller models) to 16GB+ (for large-scale edge gateways).
- **Operating System**: Linux (Kernel 6.12+), RTOS (Zephyr, FreeRTOS), or Android 15+.
- **Language**: Python 3.10+ (for simulation) or C++/Rust (for production-grade deployment).

---

## 3. Installation
The Edge TinyML suite is a lightweight Python-based core designed for simulation and hardware orchestration.

### Step 1: Clone the Project
```bash
git clone https://github.com/mriridescent/future-proofing.git
cd projects/edge_tiny_ml
```

### Step 2: Set Up Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 4. Configuration
Configuration is defined via the `QuantizationSimulator`, `NPUScheduler`, and `HardwareTarget` objects:

- **`BIT_WIDTH`**: The target precision for quantization (e.g., `BitWidth.INT4`, `BitWidth.INT8`).
- **`MAX_TOPS`**: The maximum Tera Operations Per Second of the hardware unit (default is 700.0).
- **`SRAM_MB`**: The available on-chip static RAM (default is 16MB).
- **`BATTERY_LEVEL`**: The current battery percentage (0.0 to 1.0) used for DVFS strategy.

---

## 5. Usage Guide

### Initializing the Hardware Scheduler
```python
import asyncio
from hardware import NPUScheduler, HardwareTarget, QuantizationSimulator, BitWidth

async def main():
    # Initialize the NPU scheduler
    scheduler = NPUScheduler(max_tops=700.0, sram_mb=16)

    # 1. Apply DVFS strategy based on battery level
    scheduler.battery_level = 0.45 # Low battery
    scheduler.apply_dvfs_strategy()

    # 2. Simulate 8-bit quantization on a set of model weights
    q_sim = QuantizationSimulator()
    import numpy as np
    weights = np.random.randn(1000)
    q_weights = q_sim.simulate_quantization(weights, bit_width=BitWidth.INT8)

    # 3. Schedule a task on the NPU
    if scheduler.schedule_task(model_size_mb=10.0, required_tops=50.0, target=HardwareTarget.NPU):
        # 4. Execute pipelined inference across multiple units
        pipeline = [
            {"target": HardwareTarget.NPU, "required_tops": 50.0},
            {"target": HardwareTarget.DSP, "required_tops": 20.0},
            {"target": HardwareTarget.CPU, "required_tops": 5.0}
        ]
        await scheduler.execute_pipelined_inference(pipeline)
        
        # Release the NPU load when done
        scheduler.release_task(tops=50.0)

    # 5. Get hardware energy and performance telemetry
    print("\n--- Telemetry Report ---")
    print(scheduler.get_energy_profile())

if __name__ == "__main__":
    asyncio.run(main())
```

### Understanding the Status
- **`Simulating Quantization`**: The engine is mapping high-precision weights to reduced bit-widths while monitoring MSE loss.
- **`Scheduling Task`**: The scheduler is checking TOPS and SRAM availability for a new model inference.
- **`SRAM Overflow!`**: The model size exceeds the on-chip memory, resulting in a latency penalty.
- **`Offloading Decision: YES`**: Local resources are constrained; the task should be sent to a Cloud MCP server.

---

## 6. Best Practices
- **Prioritize NPU for Tensors**: Always schedule high-TOPS tensor operations on the NPU to maximize energy efficiency.
- **Set Realistic Thermal Headroom**: Ensure that the `get_thermal_headroom()` method correctly maps to your hardware's temperature sensors.
- **Minimize Offloading**: Only offload to the cloud when local latency exceeds the mission-critical threshold or when the battery is critically low.

---

## 7. Troubleshooting
- **Scheduling Failures**: If `schedule_task` returns `False`, check if the `MAX_TOPS` value is set too low or if other high-load tasks are currently running.
- **MSE Loss too High**: If 4-bit quantization results in significant accuracy degradation, migrate to 8-bit or implement more advanced QAT techniques.
- **Power Gating Issues**: Ensure that `release_task` is called as soon as an inference cycle completes to allow the NPU to enter its zero-leakage state.

---
**Branding**: David Akpoviroro Oke (MrIridescent)  
**Support**: Future-Proofing Strategic Support Team (2026)
