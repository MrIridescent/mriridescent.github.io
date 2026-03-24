"""
Bio-Finance Engine: Bridging Biological Viability and Financial Market Strategy
Creator / Programmer: David Akpoviroro Oke (MrIridescent - The Creative Renaissance Man)
Date: 2026-03-18
"""

import math
import random

class BioFinanceEngine:
    def __init__(self, drug_name, r_and_d_cost, patent_years):
        self.drug_name = drug_name
        self.r_and_d_cost = r_and_d_cost
        self.patent_years = patent_years
        self.biological_viability = 0.0
        self.market_potential = 0.0
        self.rnpv = 0.0 # Risk-adjusted Net Present Value

    def calculate_biological_viability(self, efficacy_score, safety_score, payload_delivery_rate):
        """
        Calculates biological viability based on clinical data.
        """
        self.biological_viability = (efficacy_score * 0.5) + (safety_score * 0.3) + (payload_delivery_rate * 0.2)
        return self.biological_viability

    def model_market_competition(self, competitors_count, market_share_leaders):
        """
        Models financial impact based on market competition and patent life.
        """
        base_potential = 1000000000 # 1 Billion Base
        competition_penalty = (competitors_count * 0.05)
        self.market_potential = base_potential * (1 - competition_penalty)
        return self.market_potential

    def estimate_rnpv(self, success_probability, discount_rate):
        """
        Calculates Risk-adjusted Net Present Value (rNPV).
        """
        years = range(1, self.patent_years + 1)
        cash_flows = [(self.market_potential * self.biological_viability) / (1 + discount_rate)**t for t in years]
        total_pv = sum(cash_flows)
        self.rnpv = (total_pv * success_probability) - self.r_and_d_cost
        return self.rnpv

    def generate_strategy_report(self):
        return {
            "Drug": self.drug_name,
            "Biological Viability": f"{self.biological_viability:.2f}",
            "Market Potential": f"${self.market_potential:,.2f}",
            "rNPV": f"${self.rnpv:,.2f}",
            "Strategic Recommendation": "Proceed with clinical trials" if self.rnpv > 0 else "Pivot or Divest"
        }

if __name__ == "__main__":
    # Example usage: Peptide-Drug Conjugate (PDC)
    pdc_engine = BioFinanceEngine("Vanguard-PDC-01", r_and_d_cost=250000000, patent_years=10)
    
    # Biological Viability (using synthetic comparator ARM data)
    viability = pdc_engine.calculate_biological_viability(efficacy_score=0.85, safety_score=0.92, payload_delivery_rate=0.78)
    
    # Market Competition (modeling against leaders like AstraZeneca)
    pdc_engine.model_market_competition(competitors_count=3, market_share_leaders=0.6)
    
    # rNPV estimation for 2030 patent cliff preparation
    rnpv = pdc_engine.estimate_rnpv(success_probability=0.25, discount_rate=0.1)
    
    print("--- Bio-Finance Strategic Analysis ---")
    report = pdc_engine.generate_strategy_report()
    for key, value in report.items():
        print(f"{key}: {value}")
    print("\nAuthored by: David Akpoviroro Oke (MrIridescent)")
