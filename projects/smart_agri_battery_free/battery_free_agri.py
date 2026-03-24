# Smart Agri Battery-Free - Energy-Harvesting-Aware Irrigation
# Operates on solar/thermal/RF harvesting with context-aware sleep cycles.

import time
import random
from typing import Dict, Any

class BatteryFreeAgriSensor:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.harvest_level_mw = 40.0 # Initial harvested energy
        self.moisture_threshold = 0.35 # 35% soil moisture
        self.power_state = "IDLE"

    def adjust_sampling_rate(self) -> int:
        """Dynamic power-gating based on energy budget (2026 TinyML Standard)"""
        if self.harvest_level_mw < 33.0:
            self.power_state = "DEEP_SLEEP"
            return 3600 # Sample once per hour
        elif self.harvest_level_mw < 100.0:
            self.power_state = "ECONOMY"
            return 600 # Sample every 10 minutes
        else:
            self.power_state = "FULL_NPU"
            return 60 # Sample every minute

    def analyze_soil_intent(self, moisture: float, nutrients: Dict[str, float]) -> str:
        """On-sensor evaluation of moisture and nutrients (Offline-first)"""
        if moisture < self.moisture_threshold:
            if nutrients.get("nitrogen", 1.0) < 0.5:
                return "IRRIGATE_AND_FERTILIZE: Low moisture & nitrogen depletion."
            return "IRRIGATE: Critical moisture drop detected."
        return "STABLE: Nutrient and moisture levels optimal."

    def run_agri_cycle(self, energy_harvest: float):
        """Simulate real-world irrigation decision loop in remote areas"""
        self.harvest_level_mw = energy_harvest
        interval = self.adjust_sampling_rate()
        
        print(f"--- Node {self.node_id} Cycle ---")
        print(f"Power State: {self.power_state} | Next Sample in {interval}s")
        
        if self.power_state != "DEEP_SLEEP":
            soil_moisture = random.uniform(0.2, 0.6)
            nutrients = {"nitrogen": random.uniform(0.3, 0.9)}
            
            decision = self.analyze_soil_intent(soil_moisture, nutrients)
            print(f"TinyML Insight: {decision}")
        else:
            print("Action: Maintaining deep-sleep to preserve capacitance.")

if __name__ == "__main__":
    sensor = BatteryFreeAgriSensor(node_id="agri-node-42")
    
    # Scenario 1: Low-Light/Cloudy (Low energy harvesting)
    sensor.run_agri_cycle(25.0)
    
    print("\n")
    
    # Scenario 2: Peak Sunlight (High energy harvesting)
    sensor.run_agri_cycle(150.0)
