import asyncio
import numpy as np
import json
from typing import List, Dict, Any

class UbuntuAgent:
    """Represents a stakeholder in the communal consensus (Indaba)."""
    def __init__(self, name: str, priority_weights: Dict[str, float]):
        self.name = name
        self.weights = priority_weights  # e.g., {'growth': 0.8, 'environment': 0.2}

    async def evaluate_proposal(self, proposal: Dict[str, float]) -> float:
        """Evaluate a proposal based on stakeholder weights (Simple Utility)."""
        score = sum(proposal[k] * self.weights.get(k, 0.0) for k in proposal)
        print(f"[{self.name}] Evaluated proposal with utility: {score:.4f}")
        return score

class IndabaConsensusEngine:
    """The 'Indaba' Protocol for Communal Value Alignment."""
    def __init__(self, stakeholders: List[UbuntuAgent]):
        self.stakeholders = stakeholders
        self.consensus_threshold = 0.7  # Minimum aggregate utility for consensus

    async def find_communal_optimum(self, proposals: List[Dict[str, float]]) -> Dict[str, Any]:
        """Find the proposal that maximizes communal (not individual) benefit."""
        best_proposal = None
        max_communal_score = -1.0
        
        print(f"--- Starting 'Indaba' Consensus for {len(self.stakeholders)} Stakeholders ---")
        
        for i, prop in enumerate(proposals):
            print(f"\nChecking Proposal {i+1}: {prop}")
            
            # Evaluate the proposal across all stakeholders
            scores = await asyncio.gather(*[s.evaluate_proposal(prop) for s in self.stakeholders])
            
            # Communal Benefit = Geometric Mean (Ensures no stakeholder is completely ignored/sacrificed)
            communal_score = np.prod(scores) ** (1.0 / len(scores))
            
            print(f"Proposal {i+1} Communal Score (Geometric Mean): {communal_score:.4f}")
            
            if communal_score > max_communal_score:
                max_communal_score = communal_score
                best_proposal = prop

        print(f"\n--- Consensus Reached ---")
        print(f"Winner: {best_proposal}")
        print(f"Final Communal Strength: {max_communal_score:.4f}")
        
        return {
            "proposal": best_proposal,
            "communal_score": max_communal_score,
            "status": "APPROVED" if max_communal_score >= self.consensus_threshold else "REJECTED"
        }

async def main():
    # 1. Define Stakeholders (The "Indaba" Circle)
    community_elder = UbuntuAgent("Elder (Cultural Heritage)", {"growth": 0.2, "environment": 0.6, "heritage": 0.9})
    tech_developer = UbuntuAgent("Dev (Economic Growth)", {"growth": 0.9, "environment": 0.3, "heritage": 0.1})
    green_sentinel = UbuntuAgent("Sentinel (Environment)", {"growth": 0.1, "environment": 0.9, "heritage": 0.4})
    
    engine = IndabaConsensusEngine([community_elder, tech_developer, green_sentinel])
    
    # 2. Define Proposals (Alternative AI Behaviors)
    proposals = [
        {"growth": 0.9, "environment": 0.1, "heritage": 0.05},  # Growth-heavy (Western Style)
        {"growth": 0.2, "environment": 0.8, "heritage": 0.7},  # Conservation-heavy
        {"growth": 0.5, "environment": 0.5, "heritage": 0.6}   # Balanced (Ubuntu Style)
    ]
    
    # 3. Run the Consensus Protocol
    result = await engine.find_communal_optimum(proposals)
    
    # Output results
    with open("ubuntu_consensus_result.json", "w") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    asyncio.run(main())
