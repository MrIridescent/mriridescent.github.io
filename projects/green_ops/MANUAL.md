# Green-Ops Scheduler: Technical Manual (2026 Edition)

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
The **Green-Ops Scheduler** is the 2026 industry-leading solution for sustainable AI infrastructure. It provides a mission-critical platform for carbon-aware scheduling, dynamic workload migration, and real-time net-zero accounting for high-compute AI environments.

---

## 2. Platform Requirements
For optimal performance on green-ops nodes and cloud orchestrators:
- **Processor**: Multi-core CPU (low-latency is required for fast migration decisions).
- **Memory**: 8GB+ RAM (ECC preferred for accurate carbon accounting logs).
- **Operating System**: Linux (Kernel 6.12+), macOS (15.0+), or specialized Green-OS.
- **Connectivity**: High-bandwidth networking for cross-region workload migration.
- **Data Source**: Access to a real-time Carbon Intensity API (e.g., WattTime, Electricity Maps).

---

## 3. Installation
The Green-Ops suite is a lightweight Python-based core designed to integrate with standard cloud and Kubernetes platforms.

### Step 1: Clone the Project
```bash
git clone https://github.com/mriridescent/future-proofing.git
cd projects/green_ops
```

### Step 2: Set Up Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 4. Configuration
Configuration is defined via the `ProductionGreenScheduler`, `GreenTask`, and `GridRegion` objects:

- **`REGION`**: The current local grid region (e.g., `GridRegion.EU_CENTRAL`).
- **`CARBON_QUOTA_G`**: The daily carbon budget in grams of CO2 (default is 5000.0g).
- **`TASK_WEIGHT`**: A metric of the task's compute intensity (e.g., GPU-hours or FLOPS).
- **`DELAY_TOLERANT`**: Set to `True` for tasks that can wait for a greener grid window.

---

## 5. Usage Guide

### Initializing the Green Scheduler
```python
from scheduler import ProductionGreenScheduler, GreenTask, GridRegion, TaskPriority

# Initialize the scheduler for a specific region
scheduler = ProductionGreenScheduler(region=GridRegion.US_WEST)

# 1. Add a critical task (cannot be delayed or throttled)
scheduler.add_task(GreenTask("Safety_Audit_Loop", 100.0, TaskPriority.CRITICAL))

# 2. Add a delay-tolerant background task
scheduler.add_task(GreenTask("Model_Distillation_Batch", 2000.0, TaskPriority.STANDARD, delay_tolerant=True))

# 3. Optimize and execute the queue based on carbon intensity
# This will autonomously migrate workloads or delay tasks if needed
scheduler.optimize_and_execute()

# 4. Generate a sustainability and compliance report
report = scheduler.get_sustainability_report()
print(f"Used Carbon: {report['used_carbon_g']}g | Status: {report['compliance_status']}")
```

### Understanding the Status
- **`Queued Task`**: A new compute task has been added to the local green-ops buffer.
- **`MIGRATION: Moving workload`**: The scheduler has identified a greener grid region and is relocating the task.
- **`Delaying Task`**: A delay-tolerant task has been paused until the local grid intensity drops.
- **`CARBON QUOTA EXCEEDED!`**: The daily budget has been met; all non-critical tasks are paused.

---

## 6. Best Practices
- **Define Accurate Task Weights**: Ensure that `weight` correctly reflects the real-world energy consumption of your AI models.
- **Set Realistic Quotas**: Align your `carbon_quota_g` with your organization's net-zero targets and regional regulations.
- **Monitor Forecast Windows**: Use the `get_optimal_window()` method to plan large-scale training runs during peak solar or wind hours.

---

## 7. Troubleshooting
- **Migration Latency**: If cross-region migration is too slow, ensure that your workload context (e.g., model weights, checkpoints) is efficiently quantized before transmission.
- **Quota Lockouts**: If critical tasks are being paused, check if they are correctly marked with `TaskPriority.CRITICAL`.
- **API Disconnects**: If the Carbon Intensity API is unavailable, the scheduler defaults to a conservative "Peak-Intensity" mode to prevent quota violations.

---
**Branding**: David Akpoviroro Oke (MrIridescent)  
**Support**: Future-Proofing Strategic Support Team (2026)
