# MLE Self-Evolution Agent: Technical Manual & Step-by-Step Setup

## Overview
This manual provides the technical specifications and setup instructions for the **MLE Self-Evolution Agent**, the 2026 production-grade suite for autonomous model improvement and self-evolving AI.

### Developer/Programmer Branding
- **David Akpoviroro Oke (MrIridescent)**
- **The Creative Renaissance Man**

---

## 1. Environment & Hardware Requirements

### Minimum Specifications
- **Hardware**: AI-Optimized Workstation (e.g., NVIDIA H100 or Apple M4 Ultra).
- **RAM**: 96GB+ Unified Memory (recommended for large MoE architectures).
- **Storage**: 1TB NVMe Gen 5 SSD.
- **Runtime**: Python 3.12+, PyTorch 2.5+ (optimized for Distributed MoE).

### Server & Infrastructure
- **Agentic Mesh**: Must be connected to the broader **Agentic Mesh** to access shared expert pools and task buffers.
- **Sovereign Infrastructure**: Recommended for handling sensitive model weights and training logs.

---

## 2. Installation & Setup

### Step 1: Clone & Navigate
```bash
git clone <repository-url>
cd Future-Proofing/projects/mle_evolution_agent
```

### Step 2: Virtual Environment Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3: MCP Connection (2026 Standard)
The agent uses **Model Context Protocol (MCP)** to interact with its environment. Ensure your `mcp_config.json` is configured.
```bash
cp .mcp/example_config.json .mcp/config.json
# Edit config.json with your enterprise resource URIs
```

---

## 3. Operational Workflow

### Workflow A: Autonomous Evolution Cycle
The primary entry point is `mle_agent.py`. To initiate a cycle:
1. Initialize the `MLEEvolutionAgent` with your `target_model_id`.
2. Provide a `ModelMetrics` object containing current performance data (accuracy, latency, energy, etc.).
3. Call `execute_self_evolution_cycle()` to:
   - Evaluate performance.
   - Detect "Catastrophic Forgetting."
   - Select an **Optimization Strategy** (PEFT/LoRA, INT8, DynMoE, etc.).
   - Generate a new **Reward Hypothesis**.

### Workflow B: Real-Time DynMoE Gating
Use the `run_dyn_moe_gating()` method during model inference to dynamically scale active experts.
- Input the **Token Complexity** (0.0 to 1.0).
- The engine will output the subset of active experts (e.g., `["Language", "Logic"]`).

---

## 4. Key Commands & Running the Agent

### Start Self-Evolution Simulation
```bash
python mle_agent.py
```

### Apply Specific Optimization (Conceptual)
```python
from mle_agent import MLEEvolutionAgent, ModelMetrics

mle = MLEEvolutionAgent("DSLM-7B-V2")
metrics = get_realtime_metrics() # Accuracy, Energy, etc.

# Trigger a targeted evolution cycle
mle.execute_self_evolution_cycle(metrics)
```

---

## 5. Troubleshooting & Recommendations

- **Issue**: Catastrophic Forgetting score remains high.
  - **Fix**: Increase the frequency of `replay_mastered_skills()` calls and expand the sovereign replay buffer.
- **Issue**: DynMoE scaling is too aggressive (frequent expert switching).
  - **Fix**: Implement a "hysteresis" buffer in the gating logic to prevent rapid expert activation/deactivation.
- **Best Practice**: Use **Scaphandre** or **Green Metrics Tool** to provide accurate `energy_usage_wh` data for reward discovery.

---

## 6. Citations & References
- *David Akpoviroro Oke (2026)*: "The Self-Improving Model: Evolution vs. Static Deployment."
- *Gartner (2024)*: "The Rise of the Autonomous Developer and MLE-AI."
