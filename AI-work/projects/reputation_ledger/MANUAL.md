# Reputation Ledger (M2M Trust): Technical Manual & Step-by-Step Setup

## Overview
This manual provides the technical specifications and setup instructions for the **Reputation Ledger**, the 2026 production-grade suite for cryptographic Machine-to-Machine (M2M) trust.

### Developer/Programmer Branding
- **David Akpoviroro Oke (MrIridescent)**
- **The Creative Renaissance Man**

---

## 1. Environment & Hardware Requirements

### Minimum Specifications
- **Hardware**: Secure Enclave (TEE) Optimized (e.g., Intel SGX, AMD SEV, or Qualcomm Dragonwing TEE).
- **RAM**: 16GB DDR5 (32GB+ for high-frequency transaction nodes).
- **Storage**: 500GB NVMe SSD with hardware-level encryption.
- **Runtime**: Python 3.11+, cryptography library (v42.0+).

### Server & Infrastructure
- **Network**: High-speed, low-latency A2A mesh connection.
- **Sovereign Infrastructure**: Recommended for hosting ledger nodes to ensure data geopatriation.

---

## 2. Installation & Setup

### Step 1: Clone & Navigate
```bash
git clone <repository-url>
cd Future-Proofing/projects/reputation_ledger
```

### Step 2: Virtual Environment Setup
```bash
python -m venv venv
source venv/bin/activate
pip install cryptography
```

### Step 3: Node Identity Configuration
The ledger uses **RSA-2048** keys for signing. Ensure your node identity is established on first run.
```bash
# Optional: Setup script for automated dependency checks
chmod +x setup.sh
./setup.sh
```

---

## 3. Operational Workflow

### Workflow A: Recording Interaction Events
The primary entry point is `agent_reputation.py`. To record an event:
1. Initialize the `CryptoReputationLedger`.
2. Call `record_interaction()` with:
   - `agent_id`: The ID of the agent performing the action.
   - `action`: Descriptive action (e.g., "Optimization Study").
   - `result`: "SUCCESS" or "FAILURE".
   - `role`: "Researcher", "Executor", etc.
   - `sla_met`: Boolean (defaults to True).
3. The ledger automatically hashes the event into a **Merkle Tree**, links it to the previous block, and signs the payload with the node's private key.

### Workflow B: Reputation Scoring & Slashing
The engine automatically updates scores based on:
- **Base Result**: +10 (Researcher Success), +5 (Executor Success), -25 (Failure).
- **SLA Penalty (Slashing)**: Penalties are doubled if `sla_met` is False.
- **Decay**: All scores decay by 5% over time to reward consistent performance.

---

## 4. Key Commands & Running the Ledger

### Start Reputation Node
```bash
python agent_reputation.py
```

### Checkpoint to Public Chain (Simulated)
Use the `checkpoint_to_public_chain()` method to create a cryptographic proof of the ledger's state for external verification.
```python
from agent_reputation import CryptoReputationLedger

ledger = CryptoReputationLedger()
checkpoint_hash = ledger.checkpoint_to_public_chain()
```

---

## 5. Troubleshooting & Recommendations

- **Issue**: Block verification failure.
  - **Fix**: Check that the `previous_hash` correctly matches the SHA-256 hash of the parent block.
- **Issue**: Reputation scores drifting too low.
  - **Fix**: Adjust the `decay_rate` parameter to match the frequency of your agent interactions.
- **Best Practice**: Deploy ledger nodes in **Secure Enclaves** to protect private keys from host-level introspection.

---

## 6. Citations & References
- *David Akpoviroro Oke (2026)*: "Cryptographic Trust in the Agentic Mesh."
- *AI's 2026 Trajectory: Truth & ROI*: "Agentic Autonomy and Physical Embodiment."
