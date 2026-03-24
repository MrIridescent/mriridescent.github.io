# Psychiatric AI Companion: Personality-Aware Clinical Intervention
**Creator / Programmer:** David Akpoviroro Oke (MrIridescent)

---

## 1. Project Overview
The **Psychiatric AI Companion** is a disruptive 2026 suite for **Personality-Aware Clinical Intervention**. It implements a Neuro-Symbolic architecture (System 1/2) to provide explainable psychiatric interventions tailored to a user's "Big Five" personality vector and real-time biometric signals. The system bridges the gap between raw data and clinical insights.

---

## 2. Environment & System Specifications

### Hardware Requirements (2026 Standard)
- **CPU:** 4-core (minimum) or 8-core (recommended) for personality analysis and neuro-symbolic reasoning.
- **RAM:** 16GB (minimum).
- **Storage:** 256GB NVMe SSD for storing user-specific personality models and clinical knowledge bases.
- **Biometric Interface:** Compatible with **Wearable AI** (e.g., smart rings, watches) for heart rate variability (HRV) and sleep-cycle monitoring.

### Software Requirements
- **Operating System:** Linux (Ubuntu 22.04+ recommended), macOS 13+, or Windows 11 with WSL2.
- **Language:** Python 3.11+.
- **Dependencies:** `uuid`, `logging`, `random`.

---

## 3. Recommended Setup & Best Practices

### Installation
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/mriridescent/future-proofing.git
    cd future-proofing/projects/psychiatric_ai_companion
    ```
2.  **Run the Setup Script:**
    ```bash
    ./setup.sh
    ```
3.  **Execute the Companion:**
    ```python
    from psychiatric_companion import PsychiatricCompanion
    companion = PsychiatricCompanion(user_id="User_42")
    companion.run_intervention_cycle(hrv=65, sleep_score=0.82)
    ```

### Best Recommendations for Use
- **Gold-Standard Personality Mapping**: For the best results, use the system's "Big Five" mapping to create a high-fidelity representation of the user's personality before initiating any clinical interventions.
- **System 1/System 2 Balance**: Use the companion to bridge the gap between "System 1" (biometric-driven) and "System 2" (clinical-knowledge-driven) reasoning for a more holistic psychiatric intervention.
- **Privacy Assurance**: Ensure the companion is deployed in a secure, local environment to maintain user privacy and prevent unauthorized access to sensitive psychiatric data.
- **Hardware-Aware Inference**: Once the companion is configured, use the **QNN Workflow** (from the `qnn_hardware_optimizer` project) to deploy psychiatric models to edge NPUs like the Qualcomm Dragonwing IQ for low-power, real-time interventions.

---
**David Akpoviroro Oke (MrIridescent - The Creative Renaissance Man)**
**Date:** March 20, 2026
