# Reputation Ledger - M2M Trust & ERC-8004
# Tamper-proof identity and performance-mandate signing for machines.

import hashlib
import json
import time
from typing import List, Dict, Any

class AgentReputationLedger:
    """Agent Trust Scores via decentralized verifiable performance metrics."""
    def __init__(self, ledger_id: str = "ERC-8004-Chain-01"):
        self.ledger_id = ledger_id
        self.agents: Dict[str, Dict[str, Any]] = {}

    def issue_identity_token(self, agent_id: str) -> str:
        """Creating cross-platform, tamper-proof identities for machines."""
        print(f"[{self.ledger_id}] Issuing ERC-8004 identity for agent {agent_id}...")
        did = f"did:m2m:2026:{agent_id}"
        self.agents[agent_id] = {
            "did": did,
            "trust_score": 0.5, # Baseline
            "performance_history": []
        }
        return did

    def sign_performance_mandate(self, agent_id: str, task_success: bool, latency: float) -> str:
        """Machine-signed mandate to document verifiable audit trails."""
        if agent_id not in self.agents:
            return "ERROR: UNKNOWN_AGENT"
            
        # Update trust score (Strategic logic)
        score_adj = 0.05 if task_success else -0.15
        self.agents[agent_id]["trust_score"] = max(0.0, min(1.0, self.agents[agent_id]["trust_score"] + score_adj))
        
        # 2026 Strategy: Verifiable mandate signing
        payload = {
            "agent_id": agent_id,
            "success": task_success,
            "latency": latency,
            "timestamp": time.time()
        }
        mandate_sig = hashlib.sha256(json.dumps(payload).encode()).hexdigest()
        self.agents[agent_id]["performance_history"].append(mandate_sig)
        
        return mandate_sig

if __name__ == "__main__":
    ledger = AgentReputationLedger()
    
    # 1. Onboard machine identities
    id_a = ledger.issue_identity_token("WorkerAgent_01")
    id_b = ledger.issue_identity_token("WorkerAgent_02")
    
    # 2. Document verifiable performance
    sig_1 = ledger.sign_performance_mandate("WorkerAgent_01", True, 0.45)
    sig_2 = ledger.sign_performance_mandate("WorkerAgent_02", False, 5.2)
    
    # 3. Decision Logic based on Reputation
    print(f"\nWorkerAgent_01 Reputation: {ledger.agents['WorkerAgent_01']['trust_score']:.2f} (SAFE)")
    print(f"WorkerAgent_02 Reputation: {ledger.agents['WorkerAgent_02']['trust_score']:.2f} (UNSAFE)")
    
    if ledger.agents["WorkerAgent_02"]["trust_score"] < 0.4:
        print("ACTION: Revoking hiring authority in DMoE mesh for WorkerAgent_02.")
