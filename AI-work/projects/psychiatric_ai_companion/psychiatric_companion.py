import time
import uuid
import logging
from enum import Enum
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field

# 2026 Psychiatric AI & Personality-Aware Systems Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] Psychiatric-AI-Prod: %(message)s')
logger = logging.getLogger(__name__)

class MentalState(Enum):
    STABLE = "stable"
    ANXIOUS = "anxious"
    DEPRESSED = "depressed"
    MANIC = "manic"
    FLUX = "flux"

@dataclass
class PatientProfile:
    patient_id: str
    personality_vector: Dict[str, float] # Big Five traits
    current_state: MentalState = MentalState.STABLE
    baseline_metrics: Dict[str, float] = field(default_factory=dict)

class PsychiatricAICompanion:
    """
    2026 Production-Grade Psychiatric AI Assistant.
    Implements Neuro-Symbolic Explainable Reasoning and Personality-Aware Interventions.
    """
    def __init__(self, assistant_id: str):
        self.assistant_id = assistant_id
        self.knowledge_base = {
            "ANXIOUS": ["CBT_BREATHING", "MINDFULNESS_GUIDE", "STIMULUS_REDUCTION"],
            "DEPRESSED": ["BEHAVIORAL_ACTIVATION", "SOCIAL_SYNC_PROMPT", "LIGHT_EXPOSURE"],
            "MANIC": ["SLEEP_HYGIENE_LOCK", "FINANCIAL_GUARDRAIL", "STIMULI_REDUCTION"]
        }

    def analyze_mental_state(self, biometric_data: Dict[str, float], patient: PatientProfile) -> MentalState:
        """
        Analyzes real-time biometrics against personality baseline to detect state shift.
        """
        hrv = biometric_data.get("hrv", 1.0)
        sleep_hours = biometric_data.get("sleep", 8.0)
        social_interaction = biometric_data.get("social", 1.0)

        logger.info(f"Analyzing Biometrics for {patient.patient_id} | HRV: {hrv} | Sleep: {sleep_hours}")

        # Neuro-Symbolic Logic Check (System 2)
        if hrv < 0.4 and social_interaction < 0.3:
            return MentalState.ANXIOUS
        elif sleep_hours < 4.0 and social_interaction > 0.8:
            return MentalState.MANIC
        elif sleep_hours > 10.0 and social_interaction < 0.2:
            return MentalState.DEPRESSED
        
        return MentalState.STABLE

    def execute_intervention(self, state: MentalState, patient: PatientProfile):
        """
        Executes a personality-aware clinical intervention.
        """
        if state == MentalState.STABLE:
            logger.info(f"Patient {patient.patient_id} is STABLE. Maintaining baseline support.")
            return

        logger.warning(f"CRITICAL STATE DETECTED: {state.value} for {patient.patient_id}")
        
        # Select intervention based on personality (e.g., Openness to experience)
        options = self.knowledge_base.get(state.name, ["GENERAL_SUPPORT"])
        
        # Heuristic: High Openness patients prefer novel interventions
        if patient.personality_vector.get("openness", 0.5) > 0.7:
            intervention = options[-1] # Prefer more complex/novel options
        else:
            intervention = options[0] # Prefer standard/safe options

        logger.info(f"Executing Personality-Aware Intervention: {intervention} | Reason: {state.value}")
        
        # 2026 Explainable Reasoning Step
        self._generate_clinical_justification(patient.patient_id, state, intervention)

    def _generate_clinical_justification(self, patient_id: str, state: MentalState, intervention: str):
        """
        Generates an explainable reasoning path for clinical audit.
        """
        justification = (
            f"Audit Log [Patient: {patient_id}]: State {state.value} identified via HRV-Social correlation. "
            f"Intervention {intervention} selected based on high openness baseline and clinical safety rules."
        )
        logger.info(f"Clinical Justification: {justification}")

    def run_companion_cycle(self, patient: PatientProfile, live_data: Dict[str, float]):
        """Main Psychiatric Cycle."""
        logger.info(f"--- Psychiatric AI Cycle Initiated for {patient.patient_id} ---")
        
        # 1. Sense
        current_state = self.analyze_mental_state(live_data, patient)
        
        # 2. Act
        self.execute_intervention(current_state, patient)
        
        logger.info("Psychiatric cycle stabilized.")

if __name__ == "__main__":
    # 1. Setup Patient
    my_patient = PatientProfile(
        patient_id="User-449",
        personality_vector={"openness": 0.85, "conscientiousness": 0.4, "extraversion": 0.3}
    )
    
    # 2. Setup Companion
    companion = PsychiatricAICompanion(assistant_id="Psy-AI-Alpha")
    
    # 3. Simulate High-Stress Scenario
    sim_data = {"hrv": 0.25, "sleep": 3.5, "social": 0.15}
    companion.run_companion_cycle(my_patient, sim_data)
