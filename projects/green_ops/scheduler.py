import time
import random
import logging
import psutil
import datetime
import json
from typing import List, Dict, Any, Optional
from enum import Enum

# Configure Production Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("Green-Ops-Scheduler-Prod")

class GridRegion(Enum):
    US_WEST = "US-WEST"
    EU_CENTRAL = "EU-CENTRAL"
    ASIA_PACIFIC = "ASIA-PACIFIC"

class CarbonIntensityAPI:
    @staticmethod
    def get_intensity(region: GridRegion) -> float:
        hour = datetime.datetime.now().hour
        base = 450.0
        if 0 <= hour <= 6: return base * 0.4
        elif 10 <= hour <= 14: return base * 0.2
        return base

class TaskPriority(Enum):
    CRITICAL = 1
    STANDARD = 2
    BACKGROUND = 3

class GreenTask:
    def __init__(self, name: str, weight: float, priority: TaskPriority = TaskPriority.STANDARD, delay_tolerant: bool = False):
        self.name = name
        self.weight = weight
        self.priority = priority
        self.delay_tolerant = delay_tolerant
        self.timestamp = time.time()
        self.is_throttled = False

class ProductionGreenScheduler:
    def __init__(self, region: GridRegion = GridRegion.EU_CENTRAL):
        self.region = region
        self.queue: List[GreenTask] = []
        self.carbon_api = CarbonIntensityAPI()
        self.carbon_quota_g = 5000.0 # V2 FEATURE: Carbon Quotas
        self.used_carbon_g = 0.0

    def add_task(self, task: GreenTask):
        self.queue.append(task)
        logger.info(f"Queued '{task.name}' | Delay Tolerant: {task.delay_tolerant}")

    # V2 FEATURE: Dynamic Workload Migration
    def migrate_workload(self, target_region: GridRegion):
        current_i = self.carbon_api.get_intensity(self.region)
        target_i = self.carbon_api.get_intensity(target_region)
        
        if target_i < current_i * 0.7: # 30% greener
            logger.info(f"MIGRATION: Moving workload from {self.region.value} to {target_region.value} (Save: {current_i - target_i:.1f} gCO2/kWh)")
            self.region = target_region
            return True
        return False

    # V2 FEATURE: Predictive Grid Forecasting
    def get_optimal_window(self) -> int:
        """Returns the hour with the lowest predicted intensity."""
        # Simulated forecast: peak solar is usually at 12:00
        return 12

    def optimize_and_execute(self):
        current_intensity = self.carbon_api.get_intensity(self.region)
        logger.info(f"Grid Intensity: {current_intensity:.1f} gCO2/kWh")

        # Check Quota
        if self.used_carbon_g >= self.carbon_quota_g:
            logger.error("CARBON QUOTA EXCEEDED! Pausing all non-critical tasks.")
            self.queue = [t for t in self.queue if t.priority == TaskPriority.CRITICAL]

        # Migration Check
        for region in GridRegion:
            if region != self.region:
                if self.migrate_workload(region): break

        to_execute = []
        for task in self.queue:
            # V2: Predictive Delay
            if task.delay_tolerant and current_intensity > 250.0:
                logger.info(f"Delaying '{task.name}' for greener grid window.")
                continue
            
            if task.priority == TaskPriority.CRITICAL or current_intensity < 400.0:
                to_execute.append(task)

        for task in to_execute:
            self._execute_with_accounting(task, current_intensity)
        
        self.queue = [t for t in self.queue if t not in to_execute]

    def _execute_with_accounting(self, task: GreenTask, intensity: float):
        # Simulated carbon cost: weight * intensity * 0.001 (simplified)
        cost = (task.weight / 1000.0) * intensity
        self.used_carbon_g += cost
        logger.info(f"Executed '{task.name}' | Cost: {cost:.2f}g CO2 | Total: {self.used_carbon_g:.2f}g")

    def get_sustainability_report(self) -> Dict[str, Any]:
        return {
            "region": self.region.value,
            "used_carbon_g": round(self.used_carbon_g, 2),
            "quota_remaining_g": round(self.carbon_quota_g - self.used_carbon_g, 2),
            "compliance_status": "NET-ZERO-ALIGN" if self.used_carbon_g < self.carbon_quota_g else "QUOTA-EXCEEDED"
        }

if __name__ == "__main__":
    scheduler = ProductionGreenScheduler(region=GridRegion.US_WEST)
    
    # 1. Add tasks
    scheduler.add_task(GreenTask("Critical_Safety_Loop", 100.0, TaskPriority.CRITICAL))
    scheduler.add_task(GreenTask("Batch_Data_Training", 2000.0, TaskPriority.STANDARD, delay_tolerant=True))
    
    # 2. Run optimization
    scheduler.optimize_and_execute()
    
    print("\n--- 2026 Green-Ops Report V2 ---")
    print(json.dumps(scheduler.get_sustainability_report(), indent=2))
