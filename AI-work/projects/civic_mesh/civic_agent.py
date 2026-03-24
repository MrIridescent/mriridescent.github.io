# Civic-Mesh: Liquid Democracy Agentic Framework
# Enables autonomous community resource allocation via liquid voting agents.

import asyncio
import logging
import random
from dataclasses import dataclass
from typing import List, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] Civic-Mesh: %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Proposal:
    id: str
    description: str
    required_tokens: int
    current_votes: int = 0

class CivicAgent:
    def __init__(self, citizen_id: str, reputation: float):
        self.citizen_id = citizen_id
        self.reputation = reputation
        self.delegated_power = reputation * 1.5

    async def evaluate_proposal(self, proposal: Proposal) -> bool:
        """Evaluates proposal alignment with community values (SDG 11)."""
        logger.info(f"Agent {self.citizen_id} evaluating proposal: {proposal.description}")
        await asyncio.sleep(0.2)
        # Simulated logic: higher weight for sustainability
        is_aligned = "sustainability" in proposal.description.lower() or random.random() > 0.4
        return is_aligned

    async def cast_vote(self, proposal: Proposal, weight: float):
        """Casts weighted vote on-chain (simulated)."""
        logger.info(f"Agent {self.citizen_id} casting {weight:.2f} tokens for Proposal {proposal.id}")
        await asyncio.sleep(0.1)
        proposal.current_votes += weight

async def main():
    proposals = [
        Proposal("P-01", "Community solar microgrid for neighborhood resilience", 500),
        Proposal("P-02", "Automated vertical garden for local food security", 300)
    ]
    
    agents = [CivicAgent(f"Citizen-{i}", random.uniform(10, 100)) for i in range(5)]
    
    logger.info("--- Civic-Mesh Liquid Democracy Cycle Start ---")
    for prop in proposals:
        for agent in agents:
            if await agent.evaluate_proposal(prop):
                await agent.cast_vote(prop, agent.delegated_power)
        
        logger.info(f"Proposal {prop.id} Status: {prop.current_votes}/{prop.required_tokens} votes.")
    
    logger.info("--- Civic-Mesh Cycle Complete ---")

if __name__ == "__main__":
    asyncio.run(main())
