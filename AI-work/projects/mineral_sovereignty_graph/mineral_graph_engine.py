import asyncio
import random
import json
from typing import Dict, List, Any

class SovereignNegotiationAgent:
    """Represents a Regional Bloc (e.g., SADC) negotiating mineral exports."""
    def __init__(self, region: str, mineral: str, total_reserve: float):
        self.region = region
        self.mineral = mineral
        self.total_reserve = total_reserve
        # The 'Sovereign Floor Price' is based on global AI demand projections (mocked)
        self.floor_price = 100.0  # Base USD/unit
    
    async def calculate_fair_value(self, global_ai_growth: float) -> float:
        """Dynamically adjust floor price based on global demand."""
        # Premium = Floor * (Growth^1.5)
        premium = self.floor_price * (1.0 + (global_ai_growth ** 1.5))
        print(f"[{self.region}] Calculated Fair-Value Premium for {self.mineral}: ${premium:.2f}")
        return premium

class GlobalBuyerAgent:
    """Represents a Global Tech Company (e.g., Tesla, Apple) bidding for minerals."""
    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = budget
    
    async def place_bid(self, fair_value: float) -> float:
        """Place a bid; buyers try to bid lower but need the supply."""
        bid = fair_value * random.uniform(0.85, 1.1)
        print(f"[{self.name}] Placed a bid of ${bid:.2f}")
        return bid

class MineralGraphSovereigntyEngine:
    """Orchestrates the 'Agentic Diplomacy' Negotiation."""
    def __init__(self, sovereign: SovereignNegotiationAgent, buyers: List[GlobalBuyerAgent]):
        self.sovereign = sovereign
        self.buyers = buyers

    async def run_negotiation_round(self, global_ai_growth: float):
        """Run a single round of negotiation for mineral export."""
        print(f"--- 'Mineral-Sovereignty' Negotiation Round for {self.sovereign.mineral} ---")
        
        # 1. Sovereign Agent sets the floor based on data
        fair_value = await self.sovereign.calculate_fair_value(global_ai_growth)
        
        # 2. Buyers place bids
        bids = await asyncio.gather(*[b.place_bid(fair_value) for b in self.buyers])
        
        # 3. Decision Logic: Reject anything below fair_value
        max_bid = max(bids)
        winning_buyer = self.buyers[bids.index(max_bid)]
        
        print(f"\nEvaluating Best Bid: ${max_bid:.2f} from {winning_buyer.name}")
        
        if max_bid >= fair_value:
            print(f"Result: [APPROVED] Contract awarded to {winning_buyer.name}")
            status = "APPROVED"
        else:
            print(f"Result: [REJECTED] Bid too low. Sovereign Reserve Maintained.")
            status = "REJECTED"
            
        return {
            "mineral": self.sovereign.mineral,
            "fair_value": fair_value,
            "max_bid": max_bid,
            "winner": winning_buyer.name if status == "APPROVED" else None,
            "status": status
        }

async def main():
    # 1. Initialize Sovereign Region (DRC/SADC)
    sadc_agent = SovereignNegotiationAgent("SADC (DRC/Zambia)", "Cobalt/Lithium", 50000)
    
    # 2. Initialize Global Buyers (Global North Tech)
    buyers = [
        GlobalBuyerAgent("NeoTech Corp", 1000000),
        GlobalBuyerAgent("Global-Battery-System", 800000),
        GlobalBuyerAgent("Auto-Next-Gen", 1200000)
    ]
    
    engine = MineralGraphSovereigntyEngine(sadc_agent, buyers)
    
    # 3. Run Negotiation Simulation (AI demand scenario)
    global_demand_surge = 0.45  # 45% annual growth in AI compute demand
    result = await engine.run_negotiation_round(global_demand_surge)
    
    # Save the 'Contract Record' to disk
    with open("sovereign_contract_result.json", "w") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    asyncio.run(main())
