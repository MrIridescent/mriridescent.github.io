# Bio-Finance Engine - Bridging Biological Viability and Financial Market Strategy
# Evaluates drug candidates based on payload delivery vs. patent lifecycle.

import math
from typing import Dict, Any

class BioFinanceModel:
    def __init__(self, drug_name: str, patent_cliff_year: int):
        self.drug_name = drug_name
        self.patent_cliff = patent_cliff_year
        self.competitor_benchmarks = {
            "Enhertu": {"payload_delivery_rate": 0.85, "market_share": 0.45},
            "Keytruda": {"payload_delivery_rate": 0.78, "market_share": 0.38}
        }

    def evaluate_biological_performance(self, preclinical_results: Dict[str, float]) -> float:
        """Score drug based on tumor penetration and payload efficacy"""
        tumor_pen = preclinical_results.get("tumor_penetration", 0.0)
        payload_eff = preclinical_results.get("payload_efficacy", 0.0)
        
        # Scoring logic against market leaders (AstraZeneca/Merck)
        bio_score = (tumor_pen * 0.4) + (payload_eff * 0.6)
        print(f"Bio-Score for {self.drug_name}: {bio_score:.2f} (Target > 0.80)")
        return bio_score

    def model_financial_risk(self, bio_score: float, launch_year: int) -> float:
        """Risk-adjusted Net Present Value (rNPV) simulation"""
        years_to_cliff = self.patent_cliff - launch_year
        if years_to_cliff <= 0:
            return 0.0  # Zero ROI if launched after patent cliff
        
        # Risk factor based on biological score vs competitors
        success_probability = bio_score / 0.85  # Normalized to leader
        estimated_annual_revenue = 1.2 * (10**9) # $1.2B baseline for 2026 biotech
        
        total_revenue = estimated_annual_revenue * years_to_cliff * success_probability
        rnpv = total_revenue / math.exp(0.08 * (launch_year - 2026)) # 8% discount rate
        
        print(f"Projected rNPV: ${rnpv / 10**9:.2f}B (Risk: {100*(1-success_probability):.1f}%)")
        return rnpv

if __name__ == "__main__":
    model = BioFinanceModel("PDC-Alpha", 2035)
    
    # Preclinical data for Peptide-Drug Conjugate (PDC)
    biometrics = {
        "tumor_penetration": 0.88,
        "payload_efficacy": 0.92
    }
    
    score = model.evaluate_biological_performance(biometrics)
    rnpv = model.model_financial_risk(score, 2028)
    
    print("\nBio-Finance Strategic Outcome:")
    if score > 0.85 and rnpv > 5.0 * 10**9:
        print("ACTION: Proceed with Phase II acceleration. Strategic fit: HIGH.")
    else:
        print("ACTION: Pivot research or seek strategic partnership.")
