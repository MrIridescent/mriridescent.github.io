# M2M Social Contract - Agent Reputation Ledger
# Implements verifiable performance metrics for autonomous machine interactions (ERC-8004 mock).

import time
import hashlib
from typing import Dict, Any, List

class ReputationLedger:
    def __init__(self):
        self.ledger: Dict[str, Dict[str, Any]] = {}

    def register_agent(self, agent_id: str, specialty: str):
        """Standardized onboarding for any MCP-compatible agent"""
        self.ledger[agent_id] = {
            "specialty": specialty,
            "reputation_score": 0.5, # Baseline trust score
            "successful_tasks": 0,
            "total_tasks": 0,
            "mandates": []
        }
        print(f"Agent Registered: {agent_id} ({specialty})")

    def submit_performance_proof(self, agent_id: str, success: bool, metadata: str):
        """Update reputation based on verifiable task outcomes"""
        if agent_id not in self.ledger:
            return False
            
        self.ledger[agent_id]["total_tasks"] += 1
        if success:
            self.ledger[agent_id]["successful_tasks"] += 1
            # 2026 Logic: Incremental trust gain
            self.ledger[agent_id]["reputation_score"] = min(1.0, self.ledger[agent_id]["reputation_score"] + 0.05)
        else:
            # Harsh penalty for mission-critical failure
            self.ledger[agent_id]["reputation_score"] = max(0.0, self.ledger[agent_id]["reputation_score"] - 0.2)
            
        # Machine-signed mandate entry
        entry = f"{agent_id}:{success}:{metadata}:{time.time()}"
        mandate_hash = hashlib.sha256(entry.encode()).hexdigest()
        self.ledger[agent_id]["mandates"].append(mandate_hash)
        
        return True

    def get_trust_level(self, agent_id: str) -> float:
        return self.ledger.get(agent_id, {}).get("reputation_score", 0.0)

if __name__ == "__main__":
    ledger = ReputationLedger()
    
    # 1. Register Agents
    ledger.register_agent("Researcher_01", "Data Retrieval")
    ledger.register_agent("Executor_01", "Financial Transactions")
    
    # 2. Simulate Performance
    ledger.submit_performance_proof("Researcher_01", True, "Successfully retrieved med-legal case files.")
    ledger.submit_performance_proof("Executor_01", False, "Failed to execute hedging strategy - Latency exceed.")
    
    # 3. Decision Logic for MAS (Multi-Agent System)
    researcher_trust = ledger.get_trust_level("Researcher_01")
    executor_trust = ledger.get_trust_level("Executor_01")
    
    print(f"\nResearcher_01 Trust Score: {researcher_trust:.2f}")
    print(f"Executor_01 Trust Score: {executor_trust:.2f}")
    
    if executor_trust < 0.4:
        print("ALERT: Revoking autonomous transaction authority for Executor_01.")
